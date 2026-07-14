# Phase 1 Catalog Report

## Key Finding

MD5 verification shows that the PGFA, SMIE, and SA-DVAE repositories use byte-identical description files. Repository inspection confirms that these are the actual description files used by each method, rather than duplicated copies introduced during preprocessing. Therefore, these three methods share the same holistic LLM-generated description corpus, while STAR represents a distinct part-based description style.

Consequently, Phase 2 will compare two description groups:
- Holistic-LLM: PGFA = SMIE = SA-DVAE
- Part-based: STAR

## pgfa_description
- Coverage: 60/60
- Mean characters: 113.10
- Median characters: 114.00
- Mean tokens: 18.43
- Median tokens: 18.00

## smie_description
- Coverage: 60/60
- Mean characters: 113.10
- Median characters: 114.00
- Mean tokens: 18.43
- Median tokens: 18.00

## sa_dvae_description
- Coverage: 60/60
- Mean characters: 113.10
- Median characters: 114.00
- Mean tokens: 18.43
- Median tokens: 18.00

## star_description
- Coverage: 60/60
- Mean characters: 508.30
- Median characters: 507.00
- Mean tokens: 85.73
- Median tokens: 85.50

## Provenance Verification

- PGFA uses descriptions/ntu60_des.txt
- SMIE uses descriptions/ntu60_des.txt
- SA-DVAE uses class_lists/ntu60_llm.txt
- STAR uses text/ntu120_part_descriptions.txt

## Label Normalization

Canonical labels use names such as "Brushing hair", while STAR uses "brush hair". Only the label names were normalized; description text was left unchanged.

## Summary

- PGFA, SMIE and SA-DVAE have identical MD5 hashes.
- MD5: 811755f481a375b345dd9f2268493a0c
- STAR descriptions were extracted from the first 60 entries of ntu120_part_descriptions.txt.
- For Phase 2, PGFA, SMIE and SA-DVAE will be treated as a single Holistic-LLM group, while STAR will be treated as the Part-based group.
