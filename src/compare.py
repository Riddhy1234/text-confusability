from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr


# ============================================================
# CONFIG
# ============================================================

CATALOG_PATH = Path("data/processed/ntu60_descriptions.csv")
EMBEDDING_DIR = Path("embeddings")
REPORT_DIR = Path("reports")

ENCODERS = [
    "all-mpnet-base-v2",
    "stsb-bert-large",
]

SOURCES = {
    "Name": "canonical_name",
    "PGFA": "pgfa_description",
    "SMIE": "smie_description",
    "SA-DVAE": "sa_dvae_description",
    "STAR": "star_description",
}


# ============================================================
# LOAD CATALOG
# ============================================================

def load_catalog():
    if not CATALOG_PATH.exists():
        raise FileNotFoundError(
            f"Catalog not found: {CATALOG_PATH}"
        )

    df = pd.read_csv(CATALOG_PATH)

    if len(df) != 60:
        raise ValueError(
            f"Expected 60 NTU classes, found {len(df)}"
        )

    return df


# ============================================================
# LOAD EMBEDDINGS
# ============================================================

def load_embeddings(source, encoder):
    path = EMBEDDING_DIR / f"{source}_{encoder}.npy"

    if not path.exists():
        raise FileNotFoundError(
            f"Embedding file not found: {path}"
        )

    embeddings = np.load(path)

    if embeddings.shape[0] != 60:
        raise ValueError(
            f"{path} contains {embeddings.shape[0]} embeddings, expected 60"
        )

    return embeddings


# ============================================================
# NORMALIZE EMBEDDINGS
# ============================================================

def normalize_embeddings(embeddings):
    norms = np.linalg.norm(
        embeddings,
        axis=1,
        keepdims=True
    )

    norms[norms == 0] = 1.0

    return embeddings / norms


# ============================================================
# COSINE SIMILARITY MATRIX
# ============================================================

def similarity_matrix(embeddings):
    normalized = normalize_embeddings(embeddings)

    similarity = normalized @ normalized.T

    return similarity


# ============================================================
# DISTINCTIVENESS
# ============================================================
def compute_distinctiveness(similarity, top_k=5):
    """
    Distinctiveness = 1 - mean of the top-k off-diagonal similarities.

    Higher value = more textually distinctive.
    Lower value = more textually confusable.
    """

    n = similarity.shape[0]

    scores = []

    for i in range(n):

        other_scores = np.delete(
            similarity[i],
            i
        )

        k = min(top_k, len(other_scores))

        top_k_scores = np.sort(other_scores)[-k:]

        mean_top_k_similarity = np.mean(top_k_scores)

        distinctiveness = 1.0 - mean_top_k_similarity

        scores.append(distinctiveness)

    return np.array(scores)


# ============================================================
# TOP COMPETITORS
# ============================================================

def compute_top_competitor(similarity):
    n = similarity.shape[0]

    top1_scores = []
    top2_scores = []
    top1_indices = []
    top2_indices = []
    gaps = []

    for i in range(n):

        row = similarity[i].copy()

        # Ignore self similarity
        row[i] = -np.inf

        ranked = np.argsort(row)[::-1]

        top1 = ranked[0]
        top2 = ranked[1]

        score1 = row[top1]
        score2 = row[top2]

        gap = score1 - score2

        top1_indices.append(top1)
        top2_indices.append(top2)

        top1_scores.append(score1)
        top2_scores.append(score2)
        gaps.append(gap)

    return (
        np.array(top1_indices),
        np.array(top2_indices),
        np.array(top1_scores),
        np.array(top2_scores),
        np.array(gaps),
    )


# ============================================================
# SPEARMAN
# ============================================================

def spearman(x, y):
    result = spearmanr(x, y)

    return result.statistic


# ============================================================
# MAIN
# ============================================================

def main():

    print("\n===================================")
    print("Phase 3 Text Confusability")
    print("===================================\n")

    catalog = load_catalog()

    # Try to identify class-name column
    possible_name_columns = [
        "class_name",
        "canonical_name",
        "name",
        "action_name",
        "label_name",
    ]

    name_column = None

    for column in possible_name_columns:
        if column in catalog.columns:
            name_column = column
            break

    if name_column is None:
        name_column = catalog.columns[1]

    all_scores = {}

    detailed_rows = []

    # ========================================================
    # PROCESS EACH ENCODER
    # ========================================================

    for encoder in ENCODERS:

        print("\n-----------------------------------")
        print("Encoder:", encoder)
        print("-----------------------------------")

        encoder_scores = {}

        for source_name, source_file in SOURCES.items():

            print(
                f"Processing {source_name}..."
            )

            embeddings = load_embeddings(
                source_file,
                encoder
            )

            similarity = similarity_matrix(
                embeddings
            )

            # --------------------------------------------
            # Validation
            # --------------------------------------------

            symmetry_error = np.max(
                np.abs(
                    similarity - similarity.T
                )
            )

            diagonal_error = np.max(
                np.abs(
                    np.diag(similarity) - 1.0
                )
            )

            if symmetry_error > 1e-5:
                print(
                    "WARNING: similarity matrix is not symmetric"
                )

            if diagonal_error > 1e-5:
                print(
                    "WARNING: similarity diagonal is not 1"
                )

            # --------------------------------------------
            # Distinctiveness
            # --------------------------------------------

            distinctiveness = compute_distinctiveness(
                similarity
            )

            (
                top1_indices,
                top2_indices,
                top1_scores,
                top2_scores,
                gaps,
            ) = compute_top_competitor(
                similarity
            )

            encoder_scores[source_name] = distinctiveness

            # --------------------------------------------
            # Store per-class results
            # --------------------------------------------

            for i in range(60):

                top1_name = str(
                    catalog.iloc[
                        top1_indices[i]
                    ][name_column]
                )

                top2_name = str(
                    catalog.iloc[
                        top2_indices[i]
                    ][name_column]
                )

                detailed_rows.append({
                    "encoder": encoder,
                    "source": source_name,
                    "class_index": i + 1,
                    "class_name": str(
                        catalog.iloc[i][name_column]
                    ),
                    "distinctiveness": distinctiveness[i],
                    "top1_competitor": top1_name,
                    "top1_similarity": top1_scores[i],
                    "top2_competitor": top2_name,
                    "top2_similarity": top2_scores[i],
                    "top1_top2_gap": gaps[i],
                })

        all_scores[encoder] = encoder_scores

    # ========================================================
    # SAVE PER-CLASS CSV
    # ========================================================

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    detailed_df = pd.DataFrame(
        detailed_rows
    )

    csv_path = (
        REPORT_DIR /
        "phase3_per_class_comparison.csv"
    )

    detailed_df.to_csv(
        csv_path,
        index=False
    )

    # ========================================================
    # WRITE REPORT
    # ========================================================

    report_path = (
        REPORT_DIR /
        "phase3_findings.md"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "# Phase 3 Findings\n\n"
        )

        f.write(
            "## Objective\n\n"
        )

        f.write(
            "Phase 3 compares text confusability across "
            "multiple description sources and two sentence "
            "embedding encoders: all-mpnet-base-v2 and "
            "stsb-bert-large.\n\n"
        )

        f.write(
        
               "Distinctiveness is defined as one minus the mean "
               "cosine similarity of each class to its top-5 most "
               "similar off-diagonal NTU-60 classes. Higher values "
               "indicate more textually distinctive descriptions, "
               "while lower values indicate greater textual "
               "confusability.\n\n"
        )
        f.write(
            "The `top1_top2_gap` is defined as the similarity "
            "to the closest competing class minus the "
            "similarity to the second-closest competing class. "
            "It measures whether a class has one particularly "
            "close textual competitor or a cluster of close "
            "competitors; it is not a confidence margin.\n\n"
        )

        # ====================================================
        # ENCODER STABILITY
        # ====================================================

        f.write(
            "## Encoder Stability\n\n"
        )

        mini = all_scores["all-mpnet-base-v2"]
        bert = all_scores["stsb-bert-large"]

        for source in SOURCES.keys():

            r = spearman(
                mini[source],
                bert[source]
            )

            mean_abs_change = np.mean(
                np.abs(
                    mini[source] -
                    bert[source]
                )
            )

            f.write(
                f"- **{source}**: "
                f"Spearman = {r:.4f}, "
                f"mean absolute change = "
                f"{mean_abs_change:.4f}\n"
            )

        f.write("\n")

        # ====================================================
        # CROSS-SOURCE CORRELATIONS
        # ====================================================

        for encoder in ENCODERS:

            f.write(
                f"## Cross-Source Correlations — "
                f"{encoder}\n\n"
            )

            scores = all_scores[encoder]

            source_names = list(
                scores.keys()
            )

            for i in range(
                len(source_names)
            ):

                for j in range(
                    i + 1,
                    len(source_names)
                ):

                    a = source_names[i]
                    b = source_names[j]

                    r = spearman(
                        scores[a],
                        scores[b]
                    )

                    f.write(
                        f"- {a} vs {b}: "
                        f"Spearman = {r:.4f}\n"
                    )

            f.write("\n")

        # ====================================================
        # MOST CONFUSABLE CLASSES
        # ====================================================

        f.write(
            "## Most Textually Confusable Classes\n\n"
        )

        for encoder in ENCODERS:

            f.write(
                f"### {encoder}\n\n"
            )

            scores = all_scores[encoder]

            for source in [
                "Name",
                "SA-DVAE",
                "STAR",
            ]:

                values = scores[source]

                worst_indices = np.argsort(
                    values
                )[:10]

                f.write(
                    f"**{source}:**\n\n"
                )

                for idx in worst_indices:

                    class_name = str(
                        catalog.iloc[idx][name_column]
                    )

                    f.write(
                        f"- {class_name}: "
                        f"{values[idx]:.4f}\n"
                    )

                f.write("\n")

        # ====================================================
        # RICHER DESCRIPTION EFFECT
        # ====================================================

        f.write(
            "## Effect of Richer Descriptions\n\n"
        )

        for encoder in ENCODERS:

            f.write(
                f"### {encoder}\n\n"
            )

            name_scores = all_scores[
                encoder
            ]["Name"]

            for source in [
                "PGFA",
                "SMIE",
                "SA-DVAE",
                "STAR",
            ]:

                source_scores = all_scores[
                    encoder
                ][source]

                improvement = (
                    source_scores -
                    name_scores
                )

                mean_improvement = np.mean(
                    improvement
                )

                f.write(
                    f"- {source}: mean "
                    f"distinctiveness change vs Name = "
                    f"{mean_improvement:.4f}\n"
                )

            f.write("\n")

        # ====================================================
        # GROUNDABILITY INTERPRETATION
        # ====================================================

        f.write(
            "## Groundability Interpretation\n\n"
        )

        f.write(
            "The text-confusability analysis tests whether "
            "different textual descriptions make NTU-60 action "
            "classes more or less distinguishable in embedding "
            "space. If richer descriptions consistently produce "
            "higher distinctiveness for particular classes, they "
            "may provide more discriminative semantic information "
            "for zero-shot recognition. However, textual "
            "distinctiveness alone does not establish that a "
            "zero-shot model will recognize the class correctly; "
            "this must be validated against published per-class "
            "zero-shot accuracy.\n\n"
        )

        f.write(
            "## Published Accuracy Correlation\n\n"
        )

        f.write(
            "This section is intentionally left pending until "
            "the published per-class zero-shot accuracy values "
            "from the selected reference method are collected. "
            "The Phase 3 validation should compute Spearman "
            "correlations between per-class text-confusability "
            "metrics and the corresponding published "
            "per-class zero-shot accuracy. No accuracy values "
            "are fabricated or assumed in this analysis.\n\n"
        )

    # ========================================================
    # FINAL OUTPUT
    # ========================================================

    print("\n===================================")
    print("Phase 3 completed successfully.")
    print("===================================")

    print(
        "\nPer-class CSV written to:"
    )
    print(csv_path)

    print(
        "\nReport written to:"
    )
    print(report_path)


if __name__ == "__main__":
    main()