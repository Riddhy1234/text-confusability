# NTU-60 Text Confusability Audit

This repository implements a reproducible CPU-only text-side audit of NTU-60 action descriptions for inter-class confusability analysis.

## Scope

The project analyzes whole-class textual descriptions only. It does not train a skeleton action-recognition model or perform skeleton-to-text probing.

## Phases

### Phase 0
- Source verification and sanity checks
- CPU-only embedding verification
- Canonical NTU-60 label verification

### Phase 1
- Unified NTU-60 description catalog
- Explicit label mappings
- Per-cell text properties
- Catalog tests and coverage report

### Phase 2
- Text embeddings for multiple description sources
- Two encoders: `all-mpnet-base-v2` and `stsb-bert-large`
- 60 x 60 cosine similarity matrices
- Top-5 distinctiveness and nearest competitors
- `top1_top2_gap` analysis

### Phase 3
- Cross-source distinctiveness comparison
- Cross-encoder stability analysis
- Three required figures
- Findings report

## Description Sources

The analysis integrates five text sources:

- Canonical NTU-60 class names
- PGFA descriptions
- SMIE descriptions
- SA-DVAE descriptions
- STAR descriptions

## Key Metric

Distinctiveness is defined as 1 minus the mean cosine similarity to the top-5 most similar off-diagonal classes. Lower values indicate greater textual confusability.

`top1_top2_gap` is the similarity to the closest competing class minus the similarity to the second-closest competing class. It is not a confidence margin.

## Results

Encoder stability of per-class distinctiveness:

- Name: Spearman 0.6226
- PGFA: Spearman 0.7897
- SMIE: Spearman 0.7897
- SA-DVAE: Spearman 0.7897
- STAR: Spearman 0.6739

Detailed results are available in `reports/phase3_findings.md`.

## Figures

- `figures/ntu60_name_vs_sadvae_heatmap.png`
- `figures/ntu60_sadvae_distinctiveness.png`
- `figures/ntu60_name_vs_sadvae_scatter.png`

## Reproducibility

Embeddings are stored as NumPy arrays with JSON sidecars containing encoder information and input-content hashes. The analysis is designed to run on CPU only.

## Tests

Run:

```bash
venv\Scripts\python.exe -m pytest tests -q
```

Current project tests pass.

## Accuracy Validation

A limited validation was performed using five published per-class accuracies from Figure 5 of Li et al. (ECCV 2024), for unseen classes A1, A9, A16, A29, and A47 in a challenging random-split GZSL run. Spearman correlations are reported in `reports/phase3_findings.md`. This five-class validation is exploratory; a complete matching A1-A60 accuracy table was not available. No missing accuracy values are fabricated or assumed.

## Project Structure

```
data/
embeddings/
figures/
reports/
src/
tests/
FINDINGS.md
requirements.txt
README.md
```

## License

The repository currently does not specify a software license.
