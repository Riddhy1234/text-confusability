# Phase 3 Findings

## Objective

Phase 3 compares text confusability across multiple description sources and two sentence embedding encoders: all-mpnet-base-v2 and stsb-bert-large.

Distinctiveness is defined as one minus the mean cosine similarity of each class to its top-5 most similar off-diagonal NTU-60 classes. Higher values indicate more textually distinctive descriptions, while lower values indicate greater textual confusability.

The `top1_top2_gap` is defined as the similarity to the closest competing class minus the similarity to the second-closest competing class. It measures whether a class has one particularly close textual competitor or a cluster of close competitors; it is not a confidence margin.

## Encoder Stability

- **Name**: Spearman = 0.6226, mean absolute change = 0.0654
- **PGFA**: Spearman = 0.7897, mean absolute change = 0.0475
- **SMIE**: Spearman = 0.7897, mean absolute change = 0.0475
- **SA-DVAE**: Spearman = 0.7897, mean absolute change = 0.0475
- **STAR**: Spearman = 0.6739, mean absolute change = 0.0982

## Cross-Source Correlations — all-mpnet-base-v2

- Name vs PGFA: Spearman = 0.8052
- Name vs SMIE: Spearman = 0.8052
- Name vs SA-DVAE: Spearman = 0.8052
- Name vs STAR: Spearman = 0.4217
- PGFA vs SMIE: Spearman = 1.0000
- PGFA vs SA-DVAE: Spearman = 1.0000
- PGFA vs STAR: Spearman = 0.5101
- SMIE vs SA-DVAE: Spearman = 1.0000
- SMIE vs STAR: Spearman = 0.5101
- SA-DVAE vs STAR: Spearman = 0.5101

## Cross-Source Correlations — stsb-bert-large

- Name vs PGFA: Spearman = 0.5584
- Name vs SMIE: Spearman = 0.5584
- Name vs SA-DVAE: Spearman = 0.5584
- Name vs STAR: Spearman = 0.4533
- PGFA vs SMIE: Spearman = 1.0000
- PGFA vs SA-DVAE: Spearman = 1.0000
- PGFA vs STAR: Spearman = 0.5442
- SMIE vs SA-DVAE: Spearman = 1.0000
- SMIE vs STAR: Spearman = 0.5442
- SA-DVAE vs STAR: Spearman = 0.5442

## Most Textually Confusable Classes

### all-mpnet-base-v2

**Name:**

- Kicking other person: 0.3968
- Take off a hat/cap: 0.4012
- Touching neck (neckache): 0.4091
- Handshaking: 0.4169
- Hand waving: 0.4202
- Hugging other person: 0.4257
- Take off jacket: 0.4260
- Put on a hat/cap: 0.4291
- Punching/Slapping other person: 0.4336
- Touching head (headache): 0.4367

**SA-DVAE:**

- Handshaking: 0.3459
- Hand waving: 0.3472
- Patting on back of other person: 0.3869
- Kicking other person: 0.3879
- Clapping: 0.3887
- Touching back (backache): 0.3922
- Touching neck (neckache): 0.3938
- Take off a shoe: 0.3965
- Nod headbow: 0.4065
- Pointing to something with finger: 0.4081

**STAR:**

- Putting the palms together: 0.2270
- Standing up (from sitting position): 0.2356
- Kicking other person: 0.2430
- Pointing finger at the other person: 0.2436
- Pointing to something with finger: 0.2481
- Handshaking: 0.2490
- Kicking something: 0.2539
- Pickup: 0.2660
- Crossing hands in front (saying stop): 0.2665
- Hopping (one foot jumping): 0.2732

### stsb-bert-large

**Name:**

- Take off a hat/cap: 0.3937
- Kicking other person: 0.4063
- Take off jacket: 0.4195
- Take off a shoe: 0.4263
- Patting on back of other person: 0.4314
- Pushing other person: 0.4379
- Take off glasses: 0.4427
- Handshaking: 0.4453
- Kicking something: 0.4505
- Rubbing two hands together: 0.4519

**SA-DVAE:**

- Handshaking: 0.3237
- Putting the palms together: 0.3381
- Salute: 0.3483
- Clapping: 0.3793
- Kicking other person: 0.3876
- Pushing other person: 0.4095
- Touching head (headache): 0.4129
- Standing up (from sitting position): 0.4188
- Patting on back of other person: 0.4189
- Kicking something: 0.4258

**STAR:**

- Jumping up: 0.1195
- Kicking something: 0.1319
- Pointing to something with finger: 0.1370
- Throw: 0.1380
- Pointing finger at the other person: 0.1390
- Hopping (one foot jumping): 0.1424
- Putting the palms together: 0.1479
- Crossing hands in front (saying stop): 0.1504
- Pushing other person: 0.1544
- Kicking other person: 0.1621

## Effect of Richer Descriptions

### all-mpnet-base-v2

- PGFA: mean distinctiveness change vs Name = -0.0410
- SMIE: mean distinctiveness change vs Name = -0.0410
- SA-DVAE: mean distinctiveness change vs Name = -0.0410
- STAR: mean distinctiveness change vs Name = -0.2310

### stsb-bert-large

- PGFA: mean distinctiveness change vs Name = -0.0502
- SMIE: mean distinctiveness change vs Name = -0.0502
- SA-DVAE: mean distinctiveness change vs Name = -0.0502
- STAR: mean distinctiveness change vs Name = -0.3315

## Groundability Interpretation

The text-confusability analysis tests whether different textual descriptions make NTU-60 action classes more or less distinguishable in embedding space. If richer descriptions consistently produce higher distinctiveness for particular classes, they may provide more discriminative semantic information for zero-shot recognition. However, textual distinctiveness alone does not establish that a zero-shot model will recognize the class correctly; this must be validated against published per-class zero-shot accuracy.

## Published Accuracy Correlation

A limited validation was performed against the five per-class accuracies shown in Figure 5 of Li et al. (ECCV 2024). The paper reports these values for the unseen NTU-60 split {1, 9, 16, 29, 47} in a challenging run of its random-split GZSL experiments.

Published SA-DVAE per-class accuracies:

- A1 Drink water: 0.93
- A9 Standing up: 0.16
- A16 Wear a shoe: 0.94
- A29 Playing with phone/tablet: 0.60
- A47 Touch neck: 0.65

Using the corresponding five per-class values from this project's SA-DVAE description analysis:

| Encoder | Metric | Spearman rho | p-value | n |
|---|---|---:|---:|---:|
| all-mpnet-base-v2 | Distinctiveness vs accuracy | -0.10 | 0.873 | 5 |
| stsb-bert-large | Distinctiveness vs accuracy | 0.70 | 0.188 | 5 |
| all-mpnet-base-v2 | top1_top2_gap vs accuracy | 0.70 | 0.188 | 5 |
| stsb-bert-large | top1_top2_gap vs accuracy | 0.60 | 0.285 | 5 |

These correlations are exploratory only because the validation contains five classes and the published accuracies come from a specific challenging random-split GZSL run. They should not be interpreted as evidence of a general relationship between text confusability and zero-shot recognition accuracy.

A complete A1-A60 per-class accuracy correlation is not reported here because a matching, verified A1-A60 published accuracy table was not available. No missing accuracy values are fabricated or assumed.
