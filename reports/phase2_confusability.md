# Phase 2 Confusability Report

Phase 1 showed that PGFA, SMIE and SA-DVAE are byte-identical. Therefore they are analysed as a single Holistic-LLM group.

Encoder: stsb-bert-large

Top-K: 5

=========================================


# Holistic-LLM

## Top 15 Most Confusable Pairs

- Touching head (headache) ↔ Touching neck (neckache) : 0.8226
- Kicking something ↔ Kicking other person : 0.8164
- Salute ↔ Handshaking : 0.7788
- Putting the palms together ↔ Handshaking : 0.7531
- Drop ↔ Falling : 0.7496
- Clapping ↔ Putting the palms together : 0.7283
- Reach into pocket ↔ Touching other person's pocket : 0.7185
- Salute ↔ Putting the palms together : 0.7002
- Touching head (headache) ↔ Touching back (backache) : 0.6753
- Sneeze/cough ↔ Nausea or vomiting : 0.6751
- Reading ↔ Writing : 0.6682
- Sitting down ↔ Standing up (from sitting position) : 0.6656
- Take off jacket ↔ Take off a hat/cap : 0.6632
- Kicking other person ↔ Pushing other person : 0.6602
- Standing up (from sitting position) ↔ Jumping up : 0.6558

## Per-Class Distinctiveness

- Handshaking
  - Nearest : Salute
  - Similarity : 0.7788
  - Distinctiveness : 0.3237
  - Top1-Top2 Gap : 0.0257

- Putting the palms together
  - Nearest : Handshaking
  - Similarity : 0.7531
  - Distinctiveness : 0.3381
  - Top1-Top2 Gap : 0.0247

- Salute
  - Nearest : Handshaking
  - Similarity : 0.7788
  - Distinctiveness : 0.3483
  - Top1-Top2 Gap : 0.0786

- Clapping
  - Nearest : Putting the palms together
  - Similarity : 0.7283
  - Distinctiveness : 0.3793
  - Top1-Top2 Gap : 0.0985

- Kicking other person
  - Nearest : Kicking something
  - Similarity : 0.8164
  - Distinctiveness : 0.3876
  - Top1-Top2 Gap : 0.1562

- Pushing other person
  - Nearest : Kicking other person
  - Similarity : 0.6602
  - Distinctiveness : 0.4095
  - Top1-Top2 Gap : 0.0585

- Touching head (headache)
  - Nearest : Touching neck (neckache)
  - Similarity : 0.8226
  - Distinctiveness : 0.4129
  - Top1-Top2 Gap : 0.1473

- Standing up (from sitting position)
  - Nearest : Sitting down
  - Similarity : 0.6656
  - Distinctiveness : 0.4188
  - Top1-Top2 Gap : 0.0098

- Patting on back of other person
  - Nearest : Hugging other person
  - Similarity : 0.6208
  - Distinctiveness : 0.4189
  - Top1-Top2 Gap : 0.0209

- Kicking something
  - Nearest : Kicking other person
  - Similarity : 0.8164
  - Distinctiveness : 0.4258
  - Top1-Top2 Gap : 0.2149

- Touching neck (neckache)
  - Nearest : Touching head (headache)
  - Similarity : 0.8226
  - Distinctiveness : 0.4318
  - Top1-Top2 Gap : 0.2206

- Hugging other person
  - Nearest : Patting on back of other person
  - Similarity : 0.6208
  - Distinctiveness : 0.4425
  - Top1-Top2 Gap : 0.0194

- Take off a hat/cap
  - Nearest : Take off jacket
  - Similarity : 0.6632
  - Distinctiveness : 0.4498
  - Top1-Top2 Gap : 0.0740

- Touching back (backache)
  - Nearest : Touching head (headache)
  - Similarity : 0.6753
  - Distinctiveness : 0.4506
  - Top1-Top2 Gap : 0.0734

- Hopping (one foot jumping)
  - Nearest : Jumping up
  - Similarity : 0.6228
  - Distinctiveness : 0.4547
  - Top1-Top2 Gap : 0.0213

- Pointing finger at the other person
  - Nearest : Pushing other person
  - Similarity : 0.5849
  - Distinctiveness : 0.4577
  - Top1-Top2 Gap : 0.0353

- Falling
  - Nearest : Drop
  - Similarity : 0.7496
  - Distinctiveness : 0.4579
  - Top1-Top2 Gap : 0.1354

- Take off glasses
  - Nearest : Take off a hat/cap
  - Similarity : 0.5892
  - Distinctiveness : 0.4594
  - Top1-Top2 Gap : 0.0017

- Rubbing two hands together
  - Nearest : Putting the palms together
  - Similarity : 0.5790
  - Distinctiveness : 0.4620
  - Top1-Top2 Gap : 0.0205

- Nod headbow
  - Nearest : Salute
  - Similarity : 0.6204
  - Distinctiveness : 0.4640
  - Top1-Top2 Gap : 0.0019

- Drop
  - Nearest : Falling
  - Similarity : 0.7496
  - Distinctiveness : 0.4712
  - Top1-Top2 Gap : 0.2431

- Hand waving
  - Nearest : Handshaking
  - Similarity : 0.5640
  - Distinctiveness : 0.4738
  - Top1-Top2 Gap : 0.0067

- Take off a shoe
  - Nearest : Take off glasses
  - Similarity : 0.5875
  - Distinctiveness : 0.4764
  - Top1-Top2 Gap : 0.0149

- Take off jacket
  - Nearest : Take off a hat/cap
  - Similarity : 0.6632
  - Distinctiveness : 0.4770
  - Top1-Top2 Gap : 0.0988

- Punching/Slapping other person
  - Nearest : Kicking other person
  - Similarity : 0.6360
  - Distinctiveness : 0.4849
  - Top1-Top2 Gap : 0.0343

- Walking towards each other
  - Nearest : Pushing other person
  - Similarity : 0.5468
  - Distinctiveness : 0.4866
  - Top1-Top2 Gap : 0.0047

- Sneeze/cough
  - Nearest : Nausea or vomiting
  - Similarity : 0.6751
  - Distinctiveness : 0.4874
  - Top1-Top2 Gap : 0.1092

- Pointing to something with finger
  - Nearest : Throw
  - Similarity : 0.5354
  - Distinctiveness : 0.4999
  - Top1-Top2 Gap : 0.0229

- Wiping face
  - Nearest : Brushing teeth
  - Similarity : 0.5812
  - Distinctiveness : 0.5025
  - Top1-Top2 Gap : 0.0153

- Shake head
  - Nearest : Crossing hands in front (saying stop)
  - Similarity : 0.5633
  - Distinctiveness : 0.5041
  - Top1-Top2 Gap : 0.0209

- Jumping up
  - Nearest : Standing up (from sitting position)
  - Similarity : 0.6558
  - Distinctiveness : 0.5044
  - Top1-Top2 Gap : 0.0329

- Staggering
  - Nearest : Falling
  - Similarity : 0.6142
  - Distinctiveness : 0.5052
  - Top1-Top2 Gap : 0.1043

- Writing
  - Nearest : Reading
  - Similarity : 0.6682
  - Distinctiveness : 0.5054
  - Top1-Top2 Gap : 0.0589

- Sitting down
  - Nearest : Standing up (from sitting position)
  - Similarity : 0.6656
  - Distinctiveness : 0.5059
  - Top1-Top2 Gap : 0.1591

- Put on a hat/cap
  - Nearest : Wear on glasses
  - Similarity : 0.6254
  - Distinctiveness : 0.5083
  - Top1-Top2 Gap : 0.1336

- Touching other person's pocket
  - Nearest : Reach into pocket
  - Similarity : 0.7185
  - Distinctiveness : 0.5090
  - Top1-Top2 Gap : 0.1973

- Throw
  - Nearest : Pointing to something with finger
  - Similarity : 0.5354
  - Distinctiveness : 0.5128
  - Top1-Top2 Gap : 0.0013

- Reach into pocket
  - Nearest : Touching other person's pocket
  - Similarity : 0.7185
  - Distinctiveness : 0.5193
  - Top1-Top2 Gap : 0.2772

- Touching chest (stomachache/heart pain)
  - Nearest : Hugging other person
  - Similarity : 0.5338
  - Distinctiveness : 0.5256
  - Top1-Top2 Gap : 0.0471

- Crossing hands in front (saying stop)
  - Nearest : Shake head
  - Similarity : 0.5633
  - Distinctiveness : 0.5267
  - Top1-Top2 Gap : 0.0742

- Nausea or vomiting
  - Nearest : Sneeze/cough
  - Similarity : 0.6751
  - Distinctiveness : 0.5334
  - Top1-Top2 Gap : 0.2252

- Pickup
  - Nearest : Throw
  - Similarity : 0.4993
  - Distinctiveness : 0.5355
  - Top1-Top2 Gap : 0.0112

- Using a fan (with hand or paper)
  - Nearest : Rubbing two hands together
  - Similarity : 0.5316
  - Distinctiveness : 0.5456
  - Top1-Top2 Gap : 0.0398

- Brushing teeth
  - Nearest : Wiping face
  - Similarity : 0.5812
  - Distinctiveness : 0.5461
  - Top1-Top2 Gap : 0.1021

- Walking apart from each other
  - Nearest : Walking towards each other
  - Similarity : 0.4774
  - Distinctiveness : 0.5486
  - Top1-Top2 Gap : 0.0099

- Wear jacket
  - Nearest : Touching other person's pocket
  - Similarity : 0.5212
  - Distinctiveness : 0.5503
  - Top1-Top2 Gap : 0.0471

- Wear on glasses
  - Nearest : Put on a hat/cap
  - Similarity : 0.6254
  - Distinctiveness : 0.5509
  - Top1-Top2 Gap : 0.1894

- Typing on a keyboard
  - Nearest : Writing
  - Similarity : 0.6093
  - Distinctiveness : 0.5521
  - Top1-Top2 Gap : 0.1045

- Drink water
  - Nearest : Nod headbow
  - Similarity : 0.4873
  - Distinctiveness : 0.5557
  - Top1-Top2 Gap : 0.0128

- Playing with phone/tablet
  - Nearest : Make a phone call/Answer phone
  - Similarity : 0.5072
  - Distinctiveness : 0.5615
  - Top1-Top2 Gap : 0.0024

- Wear a shoe
  - Nearest : Take off a shoe
  - Similarity : 0.5635
  - Distinctiveness : 0.5717
  - Top1-Top2 Gap : 0.1038

- Reading
  - Nearest : Writing
  - Similarity : 0.6682
  - Distinctiveness : 0.5893
  - Top1-Top2 Gap : 0.2723

- Giving something to other person
  - Nearest : Handshaking
  - Similarity : 0.4339
  - Distinctiveness : 0.5909
  - Top1-Top2 Gap : 0.0089

- Brushing hair
  - Nearest : Brushing teeth
  - Similarity : 0.4791
  - Distinctiveness : 0.5980
  - Top1-Top2 Gap : 0.0746

- Cheer up
  - Nearest : Clapping
  - Similarity : 0.4162
  - Distinctiveness : 0.6028
  - Top1-Top2 Gap : 0.0125

- Tear up paper
  - Nearest : Take off glasses
  - Similarity : 0.4453
  - Distinctiveness : 0.6156
  - Top1-Top2 Gap : 0.0633

- Checking time (from watch)
  - Nearest : Typing on a keyboard
  - Similarity : 0.3765
  - Distinctiveness : 0.6494
  - Top1-Top2 Gap : 0.0251

- Make a phone call/Answer phone
  - Nearest : Playing with phone/tablet
  - Similarity : 0.5072
  - Distinctiveness : 0.6640
  - Top1-Top2 Gap : 0.2010

- Eat meal/snack
  - Nearest : Cheer up
  - Similarity : 0.3872
  - Distinctiveness : 0.6780
  - Top1-Top2 Gap : 0.0221

- Taking a selfie
  - Nearest : Handshaking
  - Similarity : 0.3278
  - Distinctiveness : 0.6870
  - Top1-Top2 Gap : 0.0011


# STAR

## Top 15 Most Confusable Pairs

- Pointing to something with finger ↔ Pointing finger at the other person : 0.9700
- Reach into pocket ↔ Touching other person's pocket : 0.9562
- Kicking something ↔ Kicking other person : 0.9309
- Putting the palms together ↔ Crossing hands in front (saying stop) : 0.9116
- Hopping (one foot jumping) ↔ Jumping up : 0.9088
- Wear a shoe ↔ Take off a shoe : 0.9020
- Touching back (backache) ↔ Touching neck (neckache) : 0.8933
- Throw ↔ Jumping up : 0.8890
- Throw ↔ Kicking something : 0.8849
- Wear jacket ↔ Take off jacket : 0.8846
- Jumping up ↔ Pushing other person : 0.8810
- Walking towards each other ↔ Walking apart from each other : 0.8778
- Standing up (from sitting position) ↔ Jumping up : 0.8745
- Staggering ↔ Falling : 0.8709
- Put on a hat/cap ↔ Take off a hat/cap : 0.8708

## Per-Class Distinctiveness

- Jumping up
  - Nearest : Hopping (one foot jumping)
  - Similarity : 0.9088
  - Distinctiveness : 0.1195
  - Top1-Top2 Gap : 0.0198

- Kicking something
  - Nearest : Kicking other person
  - Similarity : 0.9309
  - Distinctiveness : 0.1319
  - Top1-Top2 Gap : 0.0460

- Pointing to something with finger
  - Nearest : Pointing finger at the other person
  - Similarity : 0.9700
  - Distinctiveness : 0.1370
  - Top1-Top2 Gap : 0.1180

- Throw
  - Nearest : Jumping up
  - Similarity : 0.8890
  - Distinctiveness : 0.1380
  - Top1-Top2 Gap : 0.0041

- Pointing finger at the other person
  - Nearest : Pointing to something with finger
  - Similarity : 0.9700
  - Distinctiveness : 0.1390
  - Top1-Top2 Gap : 0.1220

- Hopping (one foot jumping)
  - Nearest : Jumping up
  - Similarity : 0.9088
  - Distinctiveness : 0.1424
  - Top1-Top2 Gap : 0.0465

- Putting the palms together
  - Nearest : Crossing hands in front (saying stop)
  - Similarity : 0.9116
  - Distinctiveness : 0.1479
  - Top1-Top2 Gap : 0.0416

- Crossing hands in front (saying stop)
  - Nearest : Putting the palms together
  - Similarity : 0.9116
  - Distinctiveness : 0.1504
  - Top1-Top2 Gap : 0.0659

- Pushing other person
  - Nearest : Jumping up
  - Similarity : 0.8810
  - Distinctiveness : 0.1544
  - Top1-Top2 Gap : 0.0383

- Kicking other person
  - Nearest : Kicking something
  - Similarity : 0.9309
  - Distinctiveness : 0.1621
  - Top1-Top2 Gap : 0.1018

- Rubbing two hands together
  - Nearest : Putting the palms together
  - Similarity : 0.8700
  - Distinctiveness : 0.1664
  - Top1-Top2 Gap : 0.0243

- Standing up (from sitting position)
  - Nearest : Jumping up
  - Similarity : 0.8745
  - Distinctiveness : 0.1686
  - Top1-Top2 Gap : 0.0344

- Touching back (backache)
  - Nearest : Touching neck (neckache)
  - Similarity : 0.8933
  - Distinctiveness : 0.1728
  - Top1-Top2 Gap : 0.0531

- Take off a hat/cap
  - Nearest : Put on a hat/cap
  - Similarity : 0.8708
  - Distinctiveness : 0.1735
  - Top1-Top2 Gap : 0.0254

- Shake head
  - Nearest : Crossing hands in front (saying stop)
  - Similarity : 0.8378
  - Distinctiveness : 0.1797
  - Top1-Top2 Gap : 0.0114

- Pickup
  - Nearest : Jumping up
  - Similarity : 0.8494
  - Distinctiveness : 0.1800
  - Top1-Top2 Gap : 0.0311

- Put on a hat/cap
  - Nearest : Take off a hat/cap
  - Similarity : 0.8708
  - Distinctiveness : 0.1814
  - Top1-Top2 Gap : 0.0214

- Take off a shoe
  - Nearest : Wear a shoe
  - Similarity : 0.9020
  - Distinctiveness : 0.1821
  - Top1-Top2 Gap : 0.0566

- Touching neck (neckache)
  - Nearest : Touching back (backache)
  - Similarity : 0.8933
  - Distinctiveness : 0.1889
  - Top1-Top2 Gap : 0.0683

- Patting on back of other person
  - Nearest : Hugging other person
  - Similarity : 0.8501
  - Distinctiveness : 0.1905
  - Top1-Top2 Gap : 0.0342

- Giving something to other person
  - Nearest : Pointing to something with finger
  - Similarity : 0.8463
  - Distinctiveness : 0.1907
  - Top1-Top2 Gap : 0.0090

- Wear a shoe
  - Nearest : Take off a shoe
  - Similarity : 0.9020
  - Distinctiveness : 0.1923
  - Top1-Top2 Gap : 0.0526

- Touching other person's pocket
  - Nearest : Reach into pocket
  - Similarity : 0.9562
  - Distinctiveness : 0.1998
  - Top1-Top2 Gap : 0.1846

- Handshaking
  - Nearest : Salute
  - Similarity : 0.8173
  - Distinctiveness : 0.2010
  - Top1-Top2 Gap : 0.0041

- Touching head (headache)
  - Nearest : Touching back (backache)
  - Similarity : 0.8402
  - Distinctiveness : 0.2040
  - Top1-Top2 Gap : 0.0152

- Reach into pocket
  - Nearest : Touching other person's pocket
  - Similarity : 0.9562
  - Distinctiveness : 0.2068
  - Top1-Top2 Gap : 0.1671

- Walking apart from each other
  - Nearest : Walking towards each other
  - Similarity : 0.8778
  - Distinctiveness : 0.2115
  - Top1-Top2 Gap : 0.0964

- Nod headbow
  - Nearest : Shake head
  - Similarity : 0.8094
  - Distinctiveness : 0.2152
  - Top1-Top2 Gap : 0.0225

- Touching chest (stomachache/heart pain)
  - Nearest : Touching head (headache)
  - Similarity : 0.8125
  - Distinctiveness : 0.2159
  - Top1-Top2 Gap : 0.0076

- Wear on glasses
  - Nearest : Put on a hat/cap
  - Similarity : 0.8072
  - Distinctiveness : 0.2162
  - Top1-Top2 Gap : 0.0003

- Punching/Slapping other person
  - Nearest : Kicking other person
  - Similarity : 0.8085
  - Distinctiveness : 0.2177
  - Top1-Top2 Gap : 0.0085

- Walking towards each other
  - Nearest : Walking apart from each other
  - Similarity : 0.8778
  - Distinctiveness : 0.2218
  - Top1-Top2 Gap : 0.1056

- Salute
  - Nearest : Handshaking
  - Similarity : 0.8173
  - Distinctiveness : 0.2219
  - Top1-Top2 Gap : 0.0338

- Take off jacket
  - Nearest : Wear jacket
  - Similarity : 0.8846
  - Distinctiveness : 0.2234
  - Top1-Top2 Gap : 0.0527

- Nausea or vomiting
  - Nearest : Sneeze/cough
  - Similarity : 0.8089
  - Distinctiveness : 0.2257
  - Top1-Top2 Gap : 0.0283

- Drop
  - Nearest : Pickup
  - Similarity : 0.8094
  - Distinctiveness : 0.2269
  - Top1-Top2 Gap : 0.0116

- Playing with phone/tablet
  - Nearest : Make a phone call/Answer phone
  - Similarity : 0.8134
  - Distinctiveness : 0.2294
  - Top1-Top2 Gap : 0.0384

- Sitting down
  - Nearest : Touching back (backache)
  - Similarity : 0.8014
  - Distinctiveness : 0.2351
  - Top1-Top2 Gap : 0.0274

- Clapping
  - Nearest : Patting on back of other person
  - Similarity : 0.7867
  - Distinctiveness : 0.2352
  - Top1-Top2 Gap : 0.0184

- Take off glasses
  - Nearest : Wear on glasses
  - Similarity : 0.8069
  - Distinctiveness : 0.2363
  - Top1-Top2 Gap : 0.0035

- Hugging other person
  - Nearest : Patting on back of other person
  - Similarity : 0.8501
  - Distinctiveness : 0.2406
  - Top1-Top2 Gap : 0.1046

- Hand waving
  - Nearest : Patting on back of other person
  - Similarity : 0.7703
  - Distinctiveness : 0.2412
  - Top1-Top2 Gap : 0.0056

- Using a fan (with hand or paper)
  - Nearest : Rubbing two hands together
  - Similarity : 0.8100
  - Distinctiveness : 0.2422
  - Top1-Top2 Gap : 0.0116

- Falling
  - Nearest : Staggering
  - Similarity : 0.8709
  - Distinctiveness : 0.2426
  - Top1-Top2 Gap : 0.0732

- Wear jacket
  - Nearest : Take off jacket
  - Similarity : 0.8846
  - Distinctiveness : 0.2478
  - Top1-Top2 Gap : 0.1264

- Wiping face
  - Nearest : Sneeze/cough
  - Similarity : 0.7996
  - Distinctiveness : 0.2555
  - Top1-Top2 Gap : 0.0550

- Writing
  - Nearest : Reading
  - Similarity : 0.8446
  - Distinctiveness : 0.2616
  - Top1-Top2 Gap : 0.0407

- Staggering
  - Nearest : Falling
  - Similarity : 0.8709
  - Distinctiveness : 0.2640
  - Top1-Top2 Gap : 0.1263

- Taking a selfie
  - Nearest : Playing with phone/tablet
  - Similarity : 0.7750
  - Distinctiveness : 0.2681
  - Top1-Top2 Gap : 0.0427

- Make a phone call/Answer phone
  - Nearest : Playing with phone/tablet
  - Similarity : 0.8134
  - Distinctiveness : 0.2764
  - Top1-Top2 Gap : 0.1059

- Typing on a keyboard
  - Nearest : Writing
  - Similarity : 0.8039
  - Distinctiveness : 0.2771
  - Top1-Top2 Gap : 0.0735

- Checking time (from watch)
  - Nearest : Wear on glasses
  - Similarity : 0.7583
  - Distinctiveness : 0.2792
  - Top1-Top2 Gap : 0.0402

- Sneeze/cough
  - Nearest : Nausea or vomiting
  - Similarity : 0.8089
  - Distinctiveness : 0.2831
  - Top1-Top2 Gap : 0.0093

- Reading
  - Nearest : Writing
  - Similarity : 0.8446
  - Distinctiveness : 0.2969
  - Top1-Top2 Gap : 0.1248

- Tear up paper
  - Nearest : Pushing other person
  - Similarity : 0.7104
  - Distinctiveness : 0.3007
  - Top1-Top2 Gap : 0.0010

- Drink water
  - Nearest : Nausea or vomiting
  - Similarity : 0.7173
  - Distinctiveness : 0.3025
  - Top1-Top2 Gap : 0.0072

- Brushing hair
  - Nearest : Wiping face
  - Similarity : 0.6959
  - Distinctiveness : 0.3116
  - Top1-Top2 Gap : 0.0033

- Brushing teeth
  - Nearest : Wiping face
  - Similarity : 0.6988
  - Distinctiveness : 0.3626
  - Top1-Top2 Gap : 0.0062

- Eat meal/snack
  - Nearest : Nausea or vomiting
  - Similarity : 0.6817
  - Distinctiveness : 0.3632
  - Top1-Top2 Gap : 0.0399

- Cheer up
  - Nearest : Hand waving
  - Similarity : 0.6625
  - Distinctiveness : 0.3829
  - Top1-Top2 Gap : 0.0451

