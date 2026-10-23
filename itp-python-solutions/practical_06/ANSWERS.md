# Practical 6: solutions and sample outputs

Run each linked Python file with `--demo` to reproduce the samples. Omit `--demo` to enter your own inputs where requested. Comments in each program explain corrections and assumptions.

## Main 1: List matrix creation

[Python solution](main_01.py)

```text
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
First row: [1, 2, 3]
Row 2, column 3: 6
```

## Main 2: Matrix traversal

[Python solution](main_02.py)

```text
Rows:
1 2 3 
4 5 6 
7 8 9 
Columns:
1 4 7 
2 5 8 
3 6 9
```

## Main 3: Row and column sums

[Python solution](main_03.py)

```text
Rows [2]
Columns [3]
Row 1 [1 2 3]
Row 2 [4 5 6]
Row sums: [6.0, 15.0]
Column sums: [5.0, 7.0, 9.0]
```

## Main 4: Matrix addition using loops

[Python solution](main_04.py)

```text
Rows [2]
Columns [2]
A row 1 [1 2]
A row 2 [3 4]
B row 1 [1 2]
B row 2 [3 4]
[[2.0, 4.0], [6.0, 8.0]]
```

## Main 5: Transpose lists

[Python solution](main_05.py)

```text
Rows [2]
Columns [3]
Row 1 [1 2 3]
Row 2 [4 5 6]
Original: [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]] Transpose: [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]
```

## Main 6: NumPy creation

[Python solution](main_06.py)

```text
[[1 2]
 [3 4]]
Shape: (2, 2) dtype: int64
[[0. 0. 0.]
 [0. 0. 0.]]
Shape: (2, 3) dtype: float64
[[1. 1.]
 [1. 1.]
 [1. 1.]]
Shape: (3, 2) dtype: float64
```

## Main 7: NumPy indexing and slicing

[Python solution](main_07.py)

```text
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
Element [1,2]: 7
Row: [5 6 7 8]
Column: [ 3  7 11]
Slice: [[2 3]
 [6 7]]
```

## Main 8: Elementwise array arithmetic

[Python solution](main_08.py)

```text
[5 7 9] [-3 -3 -3] [ 4 10 18]
Lists concatenate with +: [1, 2, 3, 4, 5, 6]
Manual elementwise: [5, 7, 9] [-3, -3, -3] [4, 10, 18]
```

## Main 9: Array statistics

[Python solution](main_09.py)

```text
Mean: 30.0 Median: 30.0 Population SD: 14.142135623730951
```

## Main 10: Reshaping constraints

[Python solution](main_10.py)

```text
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
New dimensions must multiply to the original element count (12).
```

## Main 11: Matrix multiplication

[Python solution](main_11.py)

```text
A @ B: [[19 22]
 [43 50]]
Transpose: [[1 3]
 [2 4]]
Manual: [[19, 22], [43, 50]]
Equal: True
```

## Main 12: Student marks analysis

[Python solution](main_12.py)

```text
Per-student averages: [85.         75.         91.66666667]
Highest: 95 Lowest: 70
```

## Practice 1: Soil moisture

[Python solution](practice_01.py)

```text
Zone averages: [48.85714286 54.57142857 41.         62.42857143]
Daily averages: [49.5  51.25 51.25 51.5  52.   52.75 53.75]
Highest days: [7] Lowest days: [1]
Zone 1 highest days [4] lowest days [1]
Zone 2 highest days [6] lowest days [4]
Zone 3 highest days [7] lowest days [1]
Zone 4 highest days [7] lowest days [1]
```

## Practice 2: ICU temperature matrix

[Python solution](practice_02.py)

```text
Per-patient maxima: [100.2  98.6 102.   99.6  99. ]
Per-patient averages: [ 99.26666667  98.18333333 101.41666667  99.35        98.75      ] Overall average: 99.39333333333335
Highest-temperature patient indices: [2] Patient numbers: [3]
Worksheet labels C but values resemble F. Values retained unchanged; critical interpreted as highest temperature, no clinical threshold given.
```

## Practice 3: Room occupancy

[Python solution](practice_03.py)

```text
Busiest rooms: [2 5]
Free slots: 13 Occupancy: 67.5 %
```

## Practice 4: Brightness inversion

[Python solution](practice_04.py)

```text
[[135 120 115 105  95  85]
 [145 130 125 110 100  90]
 [155 140 135 120 110 100]
 [165 150 145 130 120 110]
 [175 160 155 140 130 120]
 [185 170 165 150 140 130]]
```

## Practice 5: Warehouse stocks

[Python solution](practice_05.py)

```text
Busiest shelf (largest stock): [4]
Max stock: 30 Shelf/bin positions: [[4 1]]
Row totals: [138 170 140 210] Column totals: [53 57 62 67 71 69 69 70 70 70]
```

## Practice 6: Traffic reshape

[Python solution](practice_06.py)

```text
[[120 135 140 150 160 155 148 170]
 [180 175 190 200 210 205 198 220]
 [230 225 240 250 245 238 230 220]]
Peak count: 250 Junction/slot: [[3 4]]
Least busy junction: [1] Average: 193.08333333333334
Only 24 values supplied: use requested 3 x 8 reshape, not 3 x 24.
```

## Practice 7: Heart rate reshape

[Python solution](practice_07.py)

```text
[[72 74 73 75 76]
 [74 73 72 78 80]
 [82 79 77 76 75]
 [74 73 72 71 70]
 [69 68 67 66 72]
 [74 76 78 80 82]
 [84 83 81 79 77]
 [75 74 73 72 71]
 [70 69 68 67 66]
 [65 72 74 76 78]
 [80 82 84 86 88]
 [85 83 81 79 77]]
```

## Practice 8: Weighted revenue

[Python solution](practice_08.py)

```text
Weighted revenue per store: [2000 2085 1720 1635 1485 1335 1185]
```

## Practice 9: Rainfall halves

[Python solution](practice_09.py)

```text
First 15 days: [[ 29  98  86  64  63 106  28  90  40  29  73 118  94  96  92]
 [ 65  42  29  76 109  26 106 103  47  83  36  96  90  55  26]
 [113  95  57 117  61  52 111  57  27  67 100  39  66  33  89]
 [ 63 101 105  59 110  49  44  88  84  34 104  40 101  20 100]
 [ 64  87  86  67 106  77  27  97  78  84  77  75  29  76 100]
 [106  48 112  49  63  86  32  76  71  99 120  87  61  61  62]
 [114  35  70  90  70  65  36  58  44  50  89  83  81  56 116]
 [ 46  92  99  65  94  47  28  29  65 111  32  66  91  40  92]]
Last 15 days: [[ 99  71  32 104  65  70  57  38 113  98  85  60 103  75  64]
 [118  65 110  88  98  96  39  56  67  70  24  75  35  95  88]
 [ 68  53  42  77  87 114  64  36 104  83  90  29  51  97 104]
 [ 99  98  87  67  91  47  98  76  66  71  77  23  34  44  31]
 [ 50  80  23  55  64 119  41  47  61 120 106  23  43 102  25]
 [102  52  36  53  22  30  29  97  92  90  66  92  36 110  70]
 [ 28  54  31  54 117  56 111  70  90  66  46  97 117  46  98]
 [ 50 101  78  75  37  66 106  21  96  69  92  86  63  51  83]]
District averages first: [73.73333333 65.93333333 72.26666667 73.46666667 75.33333333 75.53333333
 70.46666667 66.46666667] last: [75.6        74.93333333 73.26666667 67.26666667 63.93333333 65.13333333
 72.06666667 71.6       ]
Overall first: 71.65 last: 70.475 Change: -1.1750000000000114
```

## Practice 10: Terrain grid

[Python solution](practice_10.py)

```text
[[135 410 362 275 273 444 134 379 180 137]
 [311 491 395 405 387 415 305 151 436 280]
 [300 248 173 471 413 358 261 429 318 277]
 [280 191 136 322 456 125 444 431 210 353]
 [166 403 380 242 127 489 278 458 371 412]
 [404 178 245 287 299 117 319 161 398 373]
 [469 398 247 487 264 230 463 248 130 288]
 [419 175 285 152 375 290 232 190 326 368]
 [477 275 164 433 352 380 138 225 407 433]
 [274 422 437 255 460 215 196 373 355 156]]
Highest: 491 Indices: [[1 1]]
Lowest: 117 Indices: [[5 5]]
Mean: 310.71 Central 4 x 4: [[322 456 125 444]
 [242 127 489 278]
 [287 299 117 319]
 [487 264 230 463]]
```
