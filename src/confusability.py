from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# Phase 2 : Text Confusability Analysis
# ============================================================

TOP_K = 5

CSV_PATH = Path("data/processed/ntu60_descriptions.csv")
EMBEDDING_DIR = Path("embeddings")
REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)

ENCODER = "all-MiniLM-L6-v2"

# Phase 1 showed these are identical.
# We therefore analyse one Holistic-LLM group
# plus STAR separately.

SOURCES = {
    "Holistic-LLM": "pgfa_description",
    "STAR": "star_description",
}


def load_catalog():
    """
    Load NTU-60 catalog.
    """

    return pd.read_csv(CSV_PATH)


def load_embeddings(source_name):
    """
    Load one embedding matrix.
    """

    path = (
        EMBEDDING_DIR
        /
        f"{source_name}_{ENCODER}.npy"
    )

    if not path.exists():

        raise FileNotFoundError(
            f"Missing embedding:\n{path}"
        )

    embeddings = np.load(path)

    if embeddings.shape[0] != 60:

        raise ValueError(
            "Expected 60 embeddings."
        )

    return embeddings


def compute_similarity_matrix(
    embeddings,
):
    """
    Compute cosine similarity.
    """

    similarity = cosine_similarity(
        embeddings
    )

    return similarity
def validate_similarity_matrix(
    similarity,
):
    """
    Basic validation.
    """

    if not np.allclose(
        similarity,
        similarity.T,
        atol=1e-6,
    ):
        raise ValueError(
            "Similarity matrix not symmetric."
        )

    diag = np.diag(similarity)

    if not np.allclose(
        diag,
        np.ones_like(diag),
        atol=1e-6,
    ):
        raise ValueError(
            "Diagonal values are not 1."
        )
def compute_class_metrics(
    similarity,
    catalog,
):
    """
    Compute nearest neighbour,
    distinctiveness,
    and margin for every class.
    """

    rows = []

    pair_scores = []

    n = similarity.shape[0]

    for i in range(n):

        row = similarity[i].copy()

        row[i] = -1

        order = np.argsort(row)[::-1]

        top1 = order[0]
        top2 = order[1]

        top1_score = float(row[top1])
        top2_score = float(row[top2])

        topk_scores = row[order[:TOP_K]]

        distinctiveness = (
            1.0 -
            float(np.mean(topk_scores))
        )

        margin = (
            top1_score -
            top2_score
        )

        rows.append(
            {
                "class_id": i,
                "class_name": catalog.loc[i, "canonical_name"],
                "nearest_class": catalog.loc[top1, "canonical_name"],
                "nearest_similarity": top1_score,
                "distinctiveness": distinctiveness,
                "margin": margin,
            }
        )

        for j in range(i + 1, n):

            pair_scores.append(
                (
                    float(similarity[i, j]),
                    catalog.loc[i, "canonical_name"],
                    catalog.loc[j, "canonical_name"],
                )
            )

    pair_scores.sort(
        reverse=True,
        key=lambda x: x[0],
    )

    class_df = pd.DataFrame(rows)

    class_df = class_df.sort_values(
        "distinctiveness",
        ascending=True,
    )

    return pair_scores, class_df
def write_report(
    group_name,
    pair_scores,
    class_df,
    report_path,
):
    """
    Write one group's results
    into the markdown report.
    """

    with open(
        report_path,
        "a",
        encoding="utf-8",
    ) as f:

        f.write(
            f"\n# {group_name}\n\n"
        )

        f.write(
            "## Top 15 Most Confusable Pairs\n\n"
        )

        for score, c1, c2 in pair_scores[:15]:

            f.write(
                f"- {c1} ↔ {c2} : {score:.4f}\n"
            )

        f.write("\n")

        f.write(
            "## Per-Class Distinctiveness\n\n"
        )

        for _, row in class_df.iterrows():

            f.write(
                f"- {row['class_name']}\n"
            )

            f.write(
                f"  - Nearest : {row['nearest_class']}\n"
            )

            f.write(
                f"  - Similarity : {row['nearest_similarity']:.4f}\n"
            )

            f.write(
                f"  - Distinctiveness : {row['distinctiveness']:.4f}\n"
            )

            f.write(
                f"  - Margin : {row['margin']:.4f}\n\n"
            )


def initialize_report(
    report_path,
):
    """
    Create a fresh report.
    """

    with open(
        report_path,
        "w",
        encoding="utf-8",
    ) as f:

        f.write(
            "# Phase 2 Confusability Report\n\n"
        )

        f.write(
            "Phase 1 showed that PGFA, SMIE "
            "and SA-DVAE are byte-identical. "
            "Therefore they are analysed as "
            "a single Holistic-LLM group.\n\n"
        )

        f.write(
            f"Encoder: {ENCODER}\n\n"
        )

        f.write(
            f"Top-K: {TOP_K}\n\n"
        )

        f.write(
            "=========================================\n\n"
        )
def process_group(
    group_name,
    source_name,
    catalog,
    report_path,
):
     
    """ Run analysis for one group.
    """
                                

    print(f"\n========== {group_name} ==========")

    embeddings = load_embeddings(source_name)

    print("Embeddings:", embeddings.shape)

    similarity = compute_similarity_matrix(
        embeddings
    )

    validate_similarity_matrix(
        similarity
    )

    pair_scores, class_df = compute_class_metrics(
        similarity,
        catalog,
    )

    write_report(
        group_name,
        pair_scores,
        class_df,
        report_path,
    )

    print("✓ Finished", group_name)


def print_summary():

    print("\n===================================")
    print("Phase 2 completed successfully.")
    print("===================================\n")


def main():

    catalog = load_catalog()

    report_path = (
        REPORT_DIR /
        "phase2_confusability.md"
    )

    initialize_report(
        report_path
    )

    for group_name, source_name in SOURCES.items():

        process_group(
            group_name,
            source_name,
            catalog,
            report_path,
        )

    print_summary()

    print(
        "Report written to:"
    )

    print(report_path)


if __name__ == "__main__":

    try:

        main()

    except Exception as e:

        print("\n===================================")
        print("Phase 2 FAILED")
        print("===================================")

        raise e