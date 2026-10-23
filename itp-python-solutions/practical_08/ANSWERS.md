# Practical 8: solutions and sample outputs

Run each linked Python file with `--demo` to reproduce the samples. Omit `--demo` to enter your own inputs where requested. Comments in each program explain corrections and assumptions.

## Main 1: Dictionary creation

[Python solution](main_01.py)

```text
{'Name': 'Ishaan', 'Age': 18, 'Marks': 85} <class 'dict'>
Each unique key maps to a value.
```

## Main 2: Key access

[Python solution](main_02.py)

```text
Ishaan 18 85
Direct access to an absent key raises KeyError.
```

## Main 3: Get with default

[Python solution](main_03.py)

```text
Asha
Not provided
get returns the default for an absent key; indexing raises KeyError.
```

## Main 4: Add and update

[Python solution](main_04.py)

```text
{'name': 'Asha', 'marks': 95, 'city': 'Mumbai'}
```

## Main 5: Remove dictionary entries

[Python solution](main_05.py)

```text
Popped: 1
{'c': 3}
del on missing key raises KeyError.
pop without a default also raises KeyError.
Safe default
```

## Main 6: Dictionary iteration

[Python solution](main_06.py)

```text
Key: a
Key: b
Value: 1
Value: 2
a 1
b 2
```

## Main 7: Views as lists

[Python solution](main_07.py)

```text
['a', 'b'] [1, 2] [('a', 1), ('b', 2)]
```

## Main 8: Character frequency

[Python solution](main_08.py)

```text
Text [hello world]
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

## Main 9: Nested students

[Python solution](main_09.py)

```text
Asha
{'S1': {'name': 'Asha', 'marks': 92}, 'S2': {'name': 'Ravi', 'marks': 90}}
```

## Main 10: Merge dictionaries

[Python solution](main_10.py)

```text
{'x': 1, 'y': 20, 'z': 3}
The incoming value overwrites an existing matching key.
```

## Main 11: Sort dictionary

[Python solution](main_11.py)

```text
By key: {'apple': 5, 'banana': 3, 'orange': 2}
By value: {'orange': 2, 'banana': 3, 'apple': 5}
```

## Main 12: Inventory operations

[Python solution](main_12.py)

```text
{'Pen': 15, 'Pencil': 20}
```

## Practice 1: Attendance updates

[Python solution](practice_01.py)

```text
{'S101': 'Present', 'S102': 'Absent', 'S103': 'Present', 'S104': 'Present', 'S105': 'Present'}
Present: 4
```

## Practice 2: Patient temperatures

[Python solution](practice_02.py)

```text
Highest: [('P002', {'name': 'Ravi', 'temp': 101.2})]
{'P001': {'name': 'Asha', 'temp': 98.6}, 'P002': {'name': 'Ravi', 'temp': 101.2}, 'P003': {'name': 'Neha', 'temp': 100.4}}
```

## Practice 3: Drone dictionary

[Python solution](practice_03.py)

```text
Keys: ['altitude', 'speed', 'battery', 'wind_speed'] Values: [250, 45, 78, 12]
```

## Practice 4: Retail inventory

[Python solution](practice_04.py)

```text
{'Laptop': 10, 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10, 'Printer': 5}
```

## Practice 5: Token frequency

[Python solution](practice_05.py)

```text
{'python': 2, 'makes': 2, 'coding': 1, 'easy': 1, 'and': 1, 'debugging': 1, 'easier': 1}
```

## Practice 6: Predict name

[Python solution](practice_06.py)

```text
Asha
```

## Practice 7: Predict length

[Python solution](practice_07.py)

```text
3
```

## Practice 8: Predict default

[Python solution](practice_08.py)

```text
0
```

## Practice 9: Correct key quoting

[Python solution](practice_09.py)

```text
Ravi
```

## Practice 10: Correct dictionary update

[Python solution](practice_10.py)

```text
{'a': 1, 'b': 2, 'c': 3}
```
