# Practical 10: solutions and sample outputs

Run each linked Python file with `--demo` to reproduce the samples. Omit `--demo` to enter your own inputs where requested. Comments in each program explain corrections and assumptions.

## Main 1: String indexing

[Python solution](main_01.py)

```text
P g o
```

## Main 2: Basic slices

[Python solution](main_02.py)

```text
Pytho ming thonP
[start:end] includes start and excludes end; indices 2 through 7 inclusive would be [2:8].
```

## Main 3: Stepped slices

[Python solution](main_03.py)

```text
Alternate: PtoPormig
Reverse: gnimmargorPnohtyP
Step 2 takes every other character; step -1 traverses backwards.
```

## Main 4: String immutability

[Python solution](main_04.py)

```text
Strings do not support item assignment.
Python
```

## Main 5: Membership

[Python solution](main_05.py)

```text
Substring [coding]
Found
```

## Main 6: Find versus index

[Python solution](main_06.py)

```text
13 13
Missing find: -1
index raises ValueError when absent; find returns -1.
```

## Main 7: Count occurrences

[Python solution](main_07.py)

```text
a count: 6 banana count: 2
count counts non-overlapping, case-sensitive substrings.
```

## Main 8: Case methods

[Python solution](main_08.py)

```text
PYTHON MAKES CODING EASY
python makes coding easy
Python Makes Coding Easy
```

## Main 9: Strip replace format

[Python solution](main_09.py)

```text
Original: '  Python is fun  '; stripped: 'Python is fun'; replaced: Python is powerful
```

## Main 10: Split and join

[Python solution](main_10.py)

```text
['Python', 'makes', 'coding', 'easy']
Python-makes-coding-easy
```

## Main 11: Palindrome slicing

[Python solution](main_11.py)

```text
Text [Madam]
Reverse: madam
Palindrome: True
```

## Main 12: Paragraph analysis

[Python solution](main_12.py)

```text
Paragraph [Python is fun. Python makes coding fun!]
Word count: 7 Character count including spaces: 39
Most frequent words: ['python', 'fun'] Count: 2
```

## Practice 1: Chatbot text cleanup

[Python solution](practice_01.py)

```text
python makes nlp powerful
['python', 'makes', 'nlp', 'powerful']
python_makes_nlp_powerful
```

## Practice 2: Student ID masking

[Python solution](practice_02.py)

```text
STU2
1098
STU2****1098
```

## Practice 3: Flight log splitting

[Python solution](practice_03.py)

```text
Altitude: 250 Speed: 45 Battery: 78
```

## Practice 4: Password checks

[Python solution](practice_04.py)

```text
{'uppercase': True, 'lowercase': True, 'digit': True, 'special': True, 'minimum_length': True}
Valid: True
```

## Practice 5: Symptom frequency

[Python solution](practice_05.py)

```text
Fever: 3 Unique symptoms: ['fever', 'cough', 'fatigue', 'cold'] Unique count: 4
Most repeated: ['fever']
```

## Practice 6: Predict stepped slice

[Python solution](practice_06.py)

```text
toPo
```

## Practice 7: Predict normalization

[Python solution](practice_07.py)

```text
DATA_SCIENCE
```

## Practice 8: Predict reversed join

[Python solution](practice_08.py)

```text
NLP-DL-ML-AI
```

## Practice 9: Complete substring slice

[Python solution](practice_09.py)

```text
Programming
```

## Practice 10: Complete replace

[Python solution](practice_10.py)

```text
Python-makes-coding-easy
```
