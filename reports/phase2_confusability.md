# Phase 2 Confusability Report

Phase 1 showed that PGFA, SMIE and SA-DVAE are byte-identical. Therefore they are analysed as a single Holistic-LLM group.

Encoder: all-MiniLM-L6-v2

Top-K: 5

=========================================


# Holistic-LLM

## Top 15 Most Confusable Pairs

- Pointing to something with finger ↔ Pointing finger at the other person : 0.8737
- Kicking something ↔ Kicking other person : 0.8289
- Put on a hat/cap ↔ Take off a hat/cap : 0.7446
- Walking towards each other ↔ Walking apart from each other : 0.7354
- Drop ↔ Falling : 0.7271
- Sitting down ↔ Standing up (from sitting position) : 0.7225
- Punching/Slapping other person ↔ Kicking other person : 0.7172
- Brushing teeth ↔ Brushing hair : 0.6950
- Touching head (headache) ↔ Touching neck (neckache) : 0.6901
- Hand waving ↔ Handshaking : 0.6860
- Hopping (one foot jumping) ↔ Jumping up : 0.6741
- Standing up (from sitting position) ↔ Jumping up : 0.6658
- Touching back (backache) ↔ Patting on back of other person : 0.6603
- Wear jacket ↔ Take off jacket : 0.6563
- Nod headbow ↔ Salute : 0.6533

## Per-Class Distinctiveness

- Kicking other person
  - Nearest : Kicking something
  - Similarity : 0.8289
  - Distinctiveness : 0.3702
  - Margin : 0.1117

- Pointing finger at the other person
  - Nearest : Pointing to something with finger
  - Similarity : 0.8737
  - Distinctiveness : 0.3834
  - Margin : 0.2516

- Take off a hat/cap
  - Nearest : Put on a hat/cap
  - Similarity : 0.7446
  - Distinctiveness : 0.3951
  - Margin : 0.1244

- Patting on back of other person
  - Nearest : Touching back (backache)
  - Similarity : 0.6603
  - Distinctiveness : 0.4017
  - Margin : 0.0382

- Handshaking
  - Nearest : Hand waving
  - Similarity : 0.6860
  - Distinctiveness : 0.4062
  - Margin : 0.0934

- Punching/Slapping other person
  - Nearest : Kicking other person
  - Similarity : 0.7172
  - Distinctiveness : 0.4193
  - Margin : 0.1036

- Take off a shoe
  - Nearest : Take off glasses
  - Similarity : 0.6440
  - Distinctiveness : 0.4202
  - Margin : 0.0212

- Hand waving
  - Nearest : Handshaking
  - Similarity : 0.6860
  - Distinctiveness : 0.4207
  - Margin : 0.1196

- Kicking something
  - Nearest : Kicking other person
  - Similarity : 0.8289
  - Distinctiveness : 0.4236
  - Margin : 0.2411

- Salute
  - Nearest : Nod headbow
  - Similarity : 0.6533
  - Distinctiveness : 0.4269
  - Margin : 0.0744

- Pointing to something with finger
  - Nearest : Pointing finger at the other person
  - Similarity : 0.8737
  - Distinctiveness : 0.4287
  - Margin : 0.3299

- Take off jacket
  - Nearest : Wear jacket
  - Similarity : 0.6563
  - Distinctiveness : 0.4345
  - Margin : 0.0336

- Take off glasses
  - Nearest : Take off a shoe
  - Similarity : 0.6440
  - Distinctiveness : 0.4469
  - Margin : 0.0315

- Putting the palms together
  - Nearest : Handshaking
  - Similarity : 0.5926
  - Distinctiveness : 0.4482
  - Margin : 0.0084

- Rubbing two hands together
  - Nearest : Putting the palms together
  - Similarity : 0.5835
  - Distinctiveness : 0.4506
  - Margin : 0.0067

- Touching back (backache)
  - Nearest : Patting on back of other person
  - Similarity : 0.6603
  - Distinctiveness : 0.4512
  - Margin : 0.0978

- Jumping up
  - Nearest : Hopping (one foot jumping)
  - Similarity : 0.6741
  - Distinctiveness : 0.4516
  - Margin : 0.0083

- Walking towards each other
  - Nearest : Walking apart from each other
  - Similarity : 0.7354
  - Distinctiveness : 0.4557
  - Margin : 0.2117

- Put on a hat/cap
  - Nearest : Take off a hat/cap
  - Similarity : 0.7446
  - Distinctiveness : 0.4574
  - Margin : 0.2071

- Hopping (one foot jumping)
  - Nearest : Jumping up
  - Similarity : 0.6741
  - Distinctiveness : 0.4622
  - Margin : 0.0864

- Clapping
  - Nearest : Putting the palms together
  - Similarity : 0.5842
  - Distinctiveness : 0.4646
  - Margin : 0.0536

- Pushing other person
  - Nearest : Kicking other person
  - Similarity : 0.5965
  - Distinctiveness : 0.4658
  - Margin : 0.0307

- Touching other person's pocket
  - Nearest : Reach into pocket
  - Similarity : 0.6367
  - Distinctiveness : 0.4659
  - Margin : 0.0599

- Nod headbow
  - Nearest : Salute
  - Similarity : 0.6533
  - Distinctiveness : 0.4694
  - Margin : 0.0488

- Standing up (from sitting position)
  - Nearest : Sitting down
  - Similarity : 0.7225
  - Distinctiveness : 0.4790
  - Margin : 0.0566

- Touching neck (neckache)
  - Nearest : Touching head (headache)
  - Similarity : 0.6901
  - Distinctiveness : 0.4793
  - Margin : 0.1275

- Hugging other person
  - Nearest : Handshaking
  - Similarity : 0.5616
  - Distinctiveness : 0.4794
  - Margin : 0.0158

- Touching head (headache)
  - Nearest : Touching neck (neckache)
  - Similarity : 0.6901
  - Distinctiveness : 0.4909
  - Margin : 0.2153

- Crossing hands in front (saying stop)
  - Nearest : Hand waving
  - Similarity : 0.5515
  - Distinctiveness : 0.5030
  - Margin : 0.0602

- Walking apart from each other
  - Nearest : Walking towards each other
  - Similarity : 0.7354
  - Distinctiveness : 0.5066
  - Margin : 0.2593

- Shake head
  - Nearest : Nod headbow
  - Similarity : 0.6044
  - Distinctiveness : 0.5088
  - Margin : 0.1129

- Reach into pocket
  - Nearest : Touching other person's pocket
  - Similarity : 0.6367
  - Distinctiveness : 0.5135
  - Margin : 0.1463

- Touching chest (stomachache/heart pain)
  - Nearest : Touching back (backache)
  - Similarity : 0.5547
  - Distinctiveness : 0.5185
  - Margin : 0.0597

- Falling
  - Nearest : Drop
  - Similarity : 0.7271
  - Distinctiveness : 0.5202
  - Margin : 0.2463

- Wear a shoe
  - Nearest : Take off a shoe
  - Similarity : 0.5540
  - Distinctiveness : 0.5241
  - Margin : 0.0554

- Throw
  - Nearest : Hand waving
  - Similarity : 0.4935
  - Distinctiveness : 0.5298
  - Margin : 0.0006

- Drop
  - Nearest : Falling
  - Similarity : 0.7271
  - Distinctiveness : 0.5415
  - Margin : 0.2341

- Sitting down
  - Nearest : Standing up (from sitting position)
  - Similarity : 0.7225
  - Distinctiveness : 0.5542
  - Margin : 0.2354

- Wear jacket
  - Nearest : Take off jacket
  - Similarity : 0.6563
  - Distinctiveness : 0.5557
  - Margin : 0.2033

- Staggering
  - Nearest : Shake head
  - Similarity : 0.4915
  - Distinctiveness : 0.5594
  - Margin : 0.0207

- Playing with phone/tablet
  - Nearest : Make a phone call/Answer phone
  - Similarity : 0.4745
  - Distinctiveness : 0.5626
  - Margin : 0.0036

- Pickup
  - Nearest : Reach into pocket
  - Similarity : 0.4863
  - Distinctiveness : 0.5664
  - Margin : 0.0163

- Brushing hair
  - Nearest : Brushing teeth
  - Similarity : 0.6950
  - Distinctiveness : 0.5815
  - Margin : 0.2895

- Giving something to other person
  - Nearest : Pushing other person
  - Similarity : 0.4799
  - Distinctiveness : 0.5904
  - Margin : 0.0532

- Wear on glasses
  - Nearest : Take off glasses
  - Similarity : 0.6125
  - Distinctiveness : 0.5956
  - Margin : 0.1324

- Wiping face
  - Nearest : Brushing teeth
  - Similarity : 0.4395
  - Distinctiveness : 0.6026
  - Margin : 0.0340

- Using a fan (with hand or paper)
  - Nearest : Rubbing two hands together
  - Similarity : 0.4919
  - Distinctiveness : 0.6114
  - Margin : 0.1220

- Brushing teeth
  - Nearest : Brushing hair
  - Similarity : 0.6950
  - Distinctiveness : 0.6209
  - Margin : 0.2555

- Typing on a keyboard
  - Nearest : Playing with phone/tablet
  - Similarity : 0.4397
  - Distinctiveness : 0.6259
  - Margin : 0.0548

- Writing
  - Nearest : Reading
  - Similarity : 0.4236
  - Distinctiveness : 0.6292
  - Margin : 0.0387

- Make a phone call/Answer phone
  - Nearest : Playing with phone/tablet
  - Similarity : 0.4745
  - Distinctiveness : 0.6417
  - Margin : 0.1332

- Nausea or vomiting
  - Nearest : Throw
  - Similarity : 0.4620
  - Distinctiveness : 0.6464
  - Margin : 0.0890

- Sneeze/cough
  - Nearest : Throw
  - Similarity : 0.3884
  - Distinctiveness : 0.6590
  - Margin : 0.0154

- Tear up paper
  - Nearest : Writing
  - Similarity : 0.3534
  - Distinctiveness : 0.6634
  - Margin : 0.0091

- Cheer up
  - Nearest : Jumping up
  - Similarity : 0.3503
  - Distinctiveness : 0.6720
  - Margin : 0.0159

- Taking a selfie
  - Nearest : Take off glasses
  - Similarity : 0.3545
  - Distinctiveness : 0.6842
  - Margin : 0.0430

- Reading
  - Nearest : Writing
  - Similarity : 0.4236
  - Distinctiveness : 0.6982
  - Margin : 0.0643

- Eat meal/snack
  - Nearest : Nausea or vomiting
  - Similarity : 0.3087
  - Distinctiveness : 0.7255
  - Margin : 0.0104

- Drink water
  - Nearest : Eat meal/snack
  - Similarity : 0.2983
  - Distinctiveness : 0.7540
  - Margin : 0.0203

- Checking time (from watch)
  - Nearest : Reading
  - Similarity : 0.2605
  - Distinctiveness : 0.7720
  - Margin : 0.0305


# STAR

## Top 15 Most Confusable Pairs

- Kicking something ↔ Kicking other person : 0.9407
- Pointing to something with finger ↔ Pointing finger at the other person : 0.9400
- Reach into pocket ↔ Touching other person's pocket : 0.8730
- Put on a hat/cap ↔ Take off a hat/cap : 0.8638
- Wear a shoe ↔ Take off a shoe : 0.8352
- Touching head (headache) ↔ Touching neck (neckache) : 0.8250
- Wear on glasses ↔ Take off glasses : 0.8186
- Touching back (backache) ↔ Touching neck (neckache) : 0.8168
- Shake head ↔ Handshaking : 0.8157
- Hopping (one foot jumping) ↔ Jumping up : 0.8067
- Drop ↔ Falling : 0.8040
- Brushing teeth ↔ Brushing hair : 0.8011
- Touching chest (stomachache/heart pain) ↔ Touching neck (neckache) : 0.7931
- Touching chest (stomachache/heart pain) ↔ Touching back (backache) : 0.7844
- Rubbing two hands together ↔ Putting the palms together : 0.7748

## Per-Class Distinctiveness

- Pointing to something with finger
  - Nearest : Pointing finger at the other person
  - Similarity : 0.9400
  - Distinctiveness : 0.2448
  - Margin : 0.1942

- Kicking other person
  - Nearest : Kicking something
  - Similarity : 0.9407
  - Distinctiveness : 0.2486
  - Margin : 0.2179

- Pointing finger at the other person
  - Nearest : Pointing to something with finger
  - Similarity : 0.9400
  - Distinctiveness : 0.2501
  - Margin : 0.2280

- Kicking something
  - Nearest : Kicking other person
  - Similarity : 0.9407
  - Distinctiveness : 0.2536
  - Margin : 0.2384

- Putting the palms together
  - Nearest : Rubbing two hands together
  - Similarity : 0.7748
  - Distinctiveness : 0.2540
  - Margin : 0.0184

- Touching neck (neckache)
  - Nearest : Touching head (headache)
  - Similarity : 0.8250
  - Distinctiveness : 0.2550
  - Margin : 0.0082

- Handshaking
  - Nearest : Shake head
  - Similarity : 0.8157
  - Distinctiveness : 0.2559
  - Margin : 0.0592

- Put on a hat/cap
  - Nearest : Take off a hat/cap
  - Similarity : 0.8638
  - Distinctiveness : 0.2578
  - Margin : 0.1309

- Take off a hat/cap
  - Nearest : Put on a hat/cap
  - Similarity : 0.8638
  - Distinctiveness : 0.2607
  - Margin : 0.1080

- Touching back (backache)
  - Nearest : Touching neck (neckache)
  - Similarity : 0.8168
  - Distinctiveness : 0.2619
  - Margin : 0.0324

- Wear a shoe
  - Nearest : Take off a shoe
  - Similarity : 0.8352
  - Distinctiveness : 0.2652
  - Margin : 0.1025

- Pushing other person
  - Nearest : Standing up (from sitting position)
  - Similarity : 0.7553
  - Distinctiveness : 0.2703
  - Margin : 0.0236

- Take off a shoe
  - Nearest : Wear a shoe
  - Similarity : 0.8352
  - Distinctiveness : 0.2724
  - Margin : 0.1129

- Standing up (from sitting position)
  - Nearest : Pushing other person
  - Similarity : 0.7553
  - Distinctiveness : 0.2799
  - Margin : 0.0214

- Touching chest (stomachache/heart pain)
  - Nearest : Touching neck (neckache)
  - Similarity : 0.7931
  - Distinctiveness : 0.2802
  - Margin : 0.0087

- Giving something to other person
  - Nearest : Pointing to something with finger
  - Similarity : 0.7457
  - Distinctiveness : 0.2808
  - Margin : 0.0180

- Jumping up
  - Nearest : Hopping (one foot jumping)
  - Similarity : 0.8067
  - Distinctiveness : 0.2865
  - Margin : 0.0728

- Rubbing two hands together
  - Nearest : Putting the palms together
  - Similarity : 0.7748
  - Distinctiveness : 0.2865
  - Margin : 0.0645

- Touching other person's pocket
  - Nearest : Reach into pocket
  - Similarity : 0.8730
  - Distinctiveness : 0.2878
  - Margin : 0.1908

- Typing on a keyboard
  - Nearest : Writing
  - Similarity : 0.7436
  - Distinctiveness : 0.2888
  - Margin : 0.0266

- Shake head
  - Nearest : Handshaking
  - Similarity : 0.8157
  - Distinctiveness : 0.2904
  - Margin : 0.1012

- Hopping (one foot jumping)
  - Nearest : Jumping up
  - Similarity : 0.8067
  - Distinctiveness : 0.2921
  - Margin : 0.0958

- Pickup
  - Nearest : Giving something to other person
  - Similarity : 0.7268
  - Distinctiveness : 0.2949
  - Margin : 0.0067

- Playing with phone/tablet
  - Nearest : Make a phone call/Answer phone
  - Similarity : 0.7220
  - Distinctiveness : 0.2958
  - Margin : 0.0050

- Wear on glasses
  - Nearest : Take off glasses
  - Similarity : 0.8186
  - Distinctiveness : 0.2963
  - Margin : 0.1225

- Take off glasses
  - Nearest : Wear on glasses
  - Similarity : 0.8186
  - Distinctiveness : 0.2973
  - Margin : 0.1092

- Writing
  - Nearest : Reading
  - Similarity : 0.7591
  - Distinctiveness : 0.2975
  - Margin : 0.0155

- Walking towards each other
  - Nearest : Walking apart from each other
  - Similarity : 0.7649
  - Distinctiveness : 0.2977
  - Margin : 0.0540

- Throw
  - Nearest : Pushing other person
  - Similarity : 0.7317
  - Distinctiveness : 0.2980
  - Margin : 0.0313

- Touching head (headache)
  - Nearest : Touching neck (neckache)
  - Similarity : 0.8250
  - Distinctiveness : 0.2984
  - Margin : 0.0906

- Take off jacket
  - Nearest : Take off a hat/cap
  - Similarity : 0.7557
  - Distinctiveness : 0.3023
  - Margin : 0.0053

- Reach into pocket
  - Nearest : Touching other person's pocket
  - Similarity : 0.8730
  - Distinctiveness : 0.3028
  - Margin : 0.2014

- Wear jacket
  - Nearest : Take off jacket
  - Similarity : 0.7505
  - Distinctiveness : 0.3114
  - Margin : 0.0176

- Walking apart from each other
  - Nearest : Walking towards each other
  - Similarity : 0.7649
  - Distinctiveness : 0.3114
  - Margin : 0.0737

- Punching/Slapping other person
  - Nearest : Kicking other person
  - Similarity : 0.7170
  - Distinctiveness : 0.3120
  - Margin : 0.0107

- Reading
  - Nearest : Writing
  - Similarity : 0.7591
  - Distinctiveness : 0.3173
  - Margin : 0.0560

- Sitting down
  - Nearest : Touching back (backache)
  - Similarity : 0.7017
  - Distinctiveness : 0.3195
  - Margin : 0.0001

- Drop
  - Nearest : Falling
  - Similarity : 0.8040
  - Distinctiveness : 0.3216
  - Margin : 0.1092

- Hand waving
  - Nearest : Handshaking
  - Similarity : 0.7426
  - Distinctiveness : 0.3250
  - Margin : 0.0760

- Crossing hands in front (saying stop)
  - Nearest : Putting the palms together
  - Similarity : 0.7543
  - Distinctiveness : 0.3255
  - Margin : 0.0791

- Nod headbow
  - Nearest : Shake head
  - Similarity : 0.7145
  - Distinctiveness : 0.3337
  - Margin : 0.0232

- Falling
  - Nearest : Drop
  - Similarity : 0.8040
  - Distinctiveness : 0.3430
  - Margin : 0.1401

- Salute
  - Nearest : Handshaking
  - Similarity : 0.6993
  - Distinctiveness : 0.3431
  - Margin : 0.0407

- Eat meal/snack
  - Nearest : Drink water
  - Similarity : 0.6748
  - Distinctiveness : 0.3533
  - Margin : 0.0251

- Nausea or vomiting
  - Nearest : Touching chest (stomachache/heart pain)
  - Similarity : 0.6569
  - Distinctiveness : 0.3533
  - Margin : 0.0037

- Staggering
  - Nearest : Hopping (one foot jumping)
  - Similarity : 0.6471
  - Distinctiveness : 0.3569
  - Margin : 0.0023

- Taking a selfie
  - Nearest : Playing with phone/tablet
  - Similarity : 0.6834
  - Distinctiveness : 0.3623
  - Margin : 0.0455

- Checking time (from watch)
  - Nearest : Playing with phone/tablet
  - Similarity : 0.6629
  - Distinctiveness : 0.3624
  - Margin : 0.0008

- Make a phone call/Answer phone
  - Nearest : Playing with phone/tablet
  - Similarity : 0.7220
  - Distinctiveness : 0.3636
  - Margin : 0.0825

- Clapping
  - Nearest : Handshaking
  - Similarity : 0.6668
  - Distinctiveness : 0.3638
  - Margin : 0.0129

- Brushing teeth
  - Nearest : Brushing hair
  - Similarity : 0.8011
  - Distinctiveness : 0.3716
  - Margin : 0.1958

- Brushing hair
  - Nearest : Brushing teeth
  - Similarity : 0.8011
  - Distinctiveness : 0.3816
  - Margin : 0.2205

- Patting on back of other person
  - Nearest : Touching back (backache)
  - Similarity : 0.6349
  - Distinctiveness : 0.3895
  - Margin : 0.0044

- Using a fan (with hand or paper)
  - Nearest : Giving something to other person
  - Similarity : 0.6197
  - Distinctiveness : 0.3973
  - Margin : 0.0058

- Hugging other person
  - Nearest : Hand waving
  - Similarity : 0.6148
  - Distinctiveness : 0.4004
  - Margin : 0.0114

- Drink water
  - Nearest : Eat meal/snack
  - Similarity : 0.6748
  - Distinctiveness : 0.4037
  - Margin : 0.0869

- Wiping face
  - Nearest : Rubbing two hands together
  - Similarity : 0.6269
  - Distinctiveness : 0.4109
  - Margin : 0.0216

- Cheer up
  - Nearest : Standing up (from sitting position)
  - Similarity : 0.6265
  - Distinctiveness : 0.4131
  - Margin : 0.0206

- Sneeze/cough
  - Nearest : Nausea or vomiting
  - Similarity : 0.5883
  - Distinctiveness : 0.4315
  - Margin : 0.0204

- Tear up paper
  - Nearest : Writing
  - Similarity : 0.6134
  - Distinctiveness : 0.4452
  - Margin : 0.0635

