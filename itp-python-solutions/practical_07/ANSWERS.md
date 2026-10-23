# Practical 7: solutions and sample outputs

Run each linked Python file with `--demo` to reproduce the samples. Omit `--demo` to enter your own inputs where requested. Comments in each program explain corrections and assumptions.

## Main 1: Lists and tuples

[Python solution](main_01.py)

```text
[1, 2, 3] <class 'list'>
('red', 'green', 'blue') <class 'tuple'>
Lists use []; tuples use commas, usually inside ().
```

## Main 2: Positive and negative indexing

[Python solution](main_02.py)

```text
First: 10 10
Last: 50 50
Middle: 30 30
First: a a
Last: e e
Middle: c c
```

## Main 3: List and tuple slices

[Python solution](main_03.py)

```text
[1, 2, 3] [4, 5] [1, 3, 5]
(1, 2, 3) (4, 5) (1, 3, 5)
Slices preserve the original sequence type; stop is exclusive.
```

## Main 4: Mutability

[Python solution](main_04.py)

```text
[9, 2, 3]
Tuples do not support item assignment.
```

## Main 5: Append and insert

[Python solution](main_05.py)

```text
['a', 'b', 'c']
['a', 'new', 'b', 'c']
```

## Main 6: Remove and pop

[Python solution](main_06.py)

```text
['a', 'c']
Popped: c
['a']
remove raises ValueError when the value is absent.
pop raises IndexError on an empty list.
```

## Main 7: Sort and reverse

[Python solution](main_07.py)

```text
Ascending: [1, 2, 3, 4]
Descending: [4, 3, 2, 1]
Reversed current order: [1, 2, 3, 4]
reverse flips the existing order; sort orders by value.
```

## Main 8: Tuple count and index

[Python solution](main_08.py)

```text
Count of 2: 2 Index of 4: 3
Missing element: index raises ValueError; count returns 0
```

## Main 9: Nested lists

[Python solution](main_09.py)

```text
3
[[1, 2], [99, 4]]
```

## Main 10: List and tuple conversion

[Python solution](main_10.py)

```text
Tuple: (1, 2, 3) Modified list: [9, 2, 3]
```

## Main 11: Sequence iteration

[Python solution](main_11.py)

```text
1
2
3
list sum: 6
1
2
3
tuple sum: 6
```

## Main 12: Shopping cart

[Python solution](main_12.py)

```text
Categories: ('Food', 'Stationery', 'Electronics') Cart: ['Bread', 'Milk'] Item count: 2
```

## Slicing 1: Matrix element indexing

[Python solution](slicing_01.py)

```text
1 9 5
```

## Slicing 2: Rows and columns

[Python solution](slicing_02.py)

```text
Second row: [4, 5, 6]
Third column:
3
6
9
Each row is a separate list; extract the column element from each row.
```

## Slicing 3: Negative matrix indices

[Python solution](slicing_03.py)

```text
Last row: [7, 8, 9] [7, 8, 9]
Last column: [3, 6, 9] [3, 6, 9]
Bottom right: 9 9
```

## Slicing 4: Row slices

[Python solution](slicing_04.py)

```text
[[1, 2, 3], [4, 5, 6]]
[[4, 5, 6], [7, 8, 9]]
```

## Slicing 5: List submatrix

[Python solution](slicing_05.py)

```text
[[1, 2], [4, 5]]
Lists do not accept matrix[:2, :2]; slice each selected row separately.
```

## Slicing 6: NumPy indices

[Python solution](slicing_06.py)

```text
Zero-based [1,2]: 6
Row: [4 5 6]
Column: [3 6 9]
```

## Slicing 7: NumPy row and column slices

[Python solution](slicing_07.py)

```text
[[1 2 3]
 [4 5 6]]
[3 6 9]
[[1, 2, 3], [4, 5, 6]]
[3, 6, 9]
```

## Slicing 8: Middle submatrix

[Python solution](slicing_08.py)

```text
[[ 6  7]
 [10 11]]
NumPy slices both axes in one expression; basic slices usually share data with the original array.
```

## Practice 1: Recent book returns

[Python solution](practice_01.py)

```text
Removed oldest: 1102
[1215, 1045, 1098, 1120, 1087, 1155, 1178, 1201, 1199, 1180, 1166, 1134]
```

## Practice 2: Drone coordinates

[Python solution](practice_02.py)

```text
x: 10 y: 20 altitude: 150
x: 15 y: 25 altitude: 160
x: 20 y: 30 altitude: 170
x: 25 y: 35 altitude: 180
x: 30 y: 40 altitude: 190
x: 35 y: 45 altitude: 200
x: 40 y: 50 altitude: 210
x: 45 y: 55 altitude: 220
x: 50 y: 60 altitude: 230
x: 55 y: 65 altitude: 240
```

## Practice 3: Doctor shifts

[Python solution](practice_03.py)

```text
1 ['Dr A', 'Dr B', 'Dr C']
2 ['Dr D', 'Dr E', 'Dr F']
3 ['Dr G', 'Dr H', 'Dr I']
4 ['Dr J', 'Dr K', 'Dr L']
5 ['Dr M', 'Dr N', 'Dr Z']
6 ['Dr P', 'Dr Q', 'Dr R']
7 ['Dr S', 'Dr T', 'Dr U']
```

## Practice 4: Deduplicate songs

[Python solution](practice_04.py)

```text
['Shape of You', 'Believer', 'Perfect', 'Faded', 'Senorita', 'Levitating', 'Blinding Lights', 'Peaches']
```

## Practice 5: Calibration tuple replacement

[Python solution](practice_05.py)

```text
Cannot modify a tuple element; replace the whole tuple in the mutable outer list.
[(0, 0), (10, 5), (25, 12), (30, 15), (40, 20)]
```

## Practice 6: Quiz score slices

[Python solution](practice_06.py)

```text
Midterm [78, 85, 91, 88] Highest: 91 Average: 85.5
Final [76, 95, 89, 84] Highest: 95 Average: 86.0
Overall [78, 85, 91, 88, 76, 95, 89, 84] Highest: 95 Average: 85.75
```

## Practice 7: Meal price sorting

[Python solution](practice_07.py)

```text
[['Sandwich', 80], ['Pizza Slice', 90], ['Noodles', 110], ['Veg Burger', 120], ['Pasta Bowl', 150]]
```

## Practice 8: GPS route slices

[Python solution](practice_08.py)

```text
Alternate: [(18.5204, 73.8567), (18.5221, 73.858), (18.5243, 73.8602), (18.5265, 73.8624), (18.5287, 73.8646)]
First five: [(18.5204, 73.8567), (18.521, 73.8575), (18.5221, 73.858), (18.5232, 73.8591), (18.5243, 73.8602)]
Reverse: [(18.5298, 73.8657), (18.5287, 73.8646), (18.5276, 73.8635), (18.5265, 73.8624), (18.5254, 73.8613), (18.5243, 73.8602), (18.5232, 73.8591), (18.5221, 73.858), (18.521, 73.8575), (18.5204, 73.8567)]
Worksheet says 20 points but supplies 10; all 10 supplied points used.
```

## Practice 9: Stock price positions

[Python solution](practice_09.py)

```text
Top three (position, price): [(10, 245), (8, 240), (9, 235)]
Lowest slots: [3] Price: 208
```

## Practice 10: Room counts

[Python solution](practice_10.py)

```text
A101 count: 2 C302 index: 7
Repeated room IDs: {'A101': 2, 'B201': 2}
Floor/category counts: {'A': 4, 'B': 4, 'C': 3}
```
