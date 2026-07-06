# Text Confusability

This repository contains the implementation for building a unified NTU-60 action description catalog by collecting and normalizing descriptions from multiple research sources.

## Phase 0
- Source verification completed
- Repository structure initialized
- Sanity checks completed

## Phase 1
- Built unified NTU-60 description catalog
- Normalized class labels
- Generated processed dataset
- Added label mapping utilities
- Added unit tests
- Generated Phase 1 report

## Project Structure

```
data/
├── normalized/
├── processed/

reports/
src/
tests/
```

## Files

- `src/phase1_build_catalog.py` – Builds the unified description catalog.
- `src/label_map.py` – Maps action labels.
- `reports/phase1_catalog.md` – Phase 1 report.
- `tests/test_label_map.py` – Unit tests.

## Requirements

```bash
pip install -r requirements.txt
```

## Repository Status

- ✅ Phase 0 Completed
- ✅ Phase 1 Completed
- ⏳ Phase 2 In Progress
