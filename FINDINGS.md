# Findings

## Summary

This project audits text-side confusability of NTU-60 action classes using five description sources and two sentence embedding encoders: all-mpnet-base-v2 and stsb-bert-large.

## Key Findings

- Textual distinctiveness is measured as 1 minus the mean similarity to the top-5 most similar off-diagonal classes. Lower distinctiveness indicates greater textual confusability.
- Name-only descriptions show substantial cross-class textual overlap.
- Richer descriptions change class-level distinctiveness, but the effect is source-dependent.
- PGFA, SMIE, and SA-DVAE show identical class-level patterns in this dataset, which is consistent with the aligned description content used for the corresponding classes.
- STAR shows a different confusability pattern from the other description sources.
- Results are reasonably stable across the two encoders, although exact values vary by encoder.
- The top1_top2_gap measures the similarity gap between the closest and second-closest competing classes. It is not a model confidence margin.

## Encoder Stability

Spearman stability between encoder-specific per-class distinctiveness:

- Name: 0.6226
- PGFA: 0.7897
- SMIE: 0.7897
- SA-DVAE: 0.7897
- STAR: 0.6739

## Important Limitation

Textual confusability does not by itself establish zero-shot recognition accuracy. A complete validation requires verified published per-class zero-shot accuracy for the same NTU-60 classes and evaluation setting. This repository does not fabricate missing accuracy values.

## Reproducibility

All reported embeddings use saved numpy artifacts with JSON sidecars containing encoder and input-content hashes. The analysis is CPU-only and the project tests currently pass.
