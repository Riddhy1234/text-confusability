from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


EMBEDDING_DIR = Path("embeddings")
REPORT_DIR = Path("reports")
FIGURE_DIR = Path("figures")

FIGURE_DIR.mkdir(parents=True, exist_ok=True)


def load_embedding(source, encoder):
    path = EMBEDDING_DIR / f"{source}_{encoder}.npy"
    return np.load(path)


def normalize(x):
    norm = np.linalg.norm(x, axis=1, keepdims=True)
    norm[norm == 0] = 1.0
    return x / norm


def similarity_matrix(x):
    x = normalize(x)
    return x @ x.T


def distinctiveness(x):
    sim = similarity_matrix(x)

    values = []

    for i in range(len(sim)):
        row = np.delete(sim[i], i)

        # Phase 2 definition: mean of top-5 competitors
        top5 = np.sort(row)[-5:]

        values.append(1.0 - np.mean(top5))

    return np.array(values)


def main():

    encoder = "stsb-bert-large"

    print("\nCreating Phase 3 figures...\n")

    # --------------------------------------------------------
    # Figure 1: Name-only vs SA-DVAE-LLM heatmap
    # --------------------------------------------------------

    name_emb = load_embedding(
        "canonical_name",
        encoder
    )

    sadvae_emb = load_embedding(
        "sa_dvae_description",
        encoder
    )

    name_sim = similarity_matrix(name_emb)
    sadvae_sim = similarity_matrix(sadvae_emb)

    # Difference between richer text and names
    diff = sadvae_sim - name_sim

    plt.figure(figsize=(10, 8))
    plt.imshow(diff, aspect="auto")
    plt.colorbar(label="Similarity change")
    plt.title(
        "NTU-60 Text Similarity Change: SA-DVAE-LLM vs Name"
    )
    plt.xlabel("Class")
    plt.ylabel("Class")
    plt.tight_layout()

    heatmap_path = (
        FIGURE_DIR /
        "ntu60_name_vs_sadvae_heatmap.png"
    )

    plt.savefig(
        heatmap_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("✓ Heatmap:", heatmap_path)

    # --------------------------------------------------------
    # Figure 2: Sorted per-class distinctiveness
    # --------------------------------------------------------

    df = pd.read_csv(
        REPORT_DIR /
        "phase3_per_class_comparison.csv"
    )

    subset = df[
        (df["encoder"] == encoder) &
        (df["source"] == "SA-DVAE")
    ].copy()

    subset = subset.sort_values(
        "distinctiveness",
        ascending=True
    )

    plt.figure(figsize=(12, 14))

    plt.barh(
        subset["class_name"],
        subset["distinctiveness"]
    )

    plt.xlabel("Distinctiveness")
    plt.ylabel("NTU-60 Class")
    plt.title(
        "NTU-60 Per-Class Text Distinctiveness — SA-DVAE"
    )

    plt.tight_layout()

    bar_path = (
        FIGURE_DIR /
        "ntu60_sadvae_distinctiveness.png"
    )

    plt.savefig(
        bar_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("✓ Bar chart:", bar_path)

    # --------------------------------------------------------
    # Figure 3: Name-only vs LLM distinctiveness
    # --------------------------------------------------------

    name_dist = distinctiveness(
        name_emb
    )

    sadvae_dist = distinctiveness(
        sadvae_emb
    )

    plt.figure(figsize=(8, 8))

    plt.scatter(
        name_dist,
        sadvae_dist
    )

    minimum = min(
        name_dist.min(),
        sadvae_dist.min()
    )

    maximum = max(
        name_dist.max(),
        sadvae_dist.max()
    )

    plt.plot(
        [minimum, maximum],
        [minimum, maximum],
        linestyle="--"
    )

    plt.xlabel(
        "Name-only Distinctiveness"
    )

    plt.ylabel(
        "SA-DVAE-LLM Distinctiveness"
    )

    plt.title(
        "Name-only vs SA-DVAE-LLM Distinctiveness"
    )

    plt.tight_layout()

    scatter_path = (
        FIGURE_DIR /
        "ntu60_name_vs_sadvae_scatter.png"
    )

    plt.savefig(
        scatter_path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print("✓ Scatter plot:", scatter_path)

    print("\n===================================")
    print("All Phase 3 figures created.")
    print("===================================")


if __name__ == "__main__":
    main()