# Practical 9: solutions and sample outputs

Run each linked Python file with `--demo` to reproduce the samples. Omit `--demo` to enter your own inputs where requested. Comments in each program explain corrections and assumptions.

## Main 1: Reusable greeting

[Python solution](main_01.py)

```text
Welcome to Python!
Welcome to Python!
Welcome to Python!
```

## Main 2: Function parameters

[Python solution](main_02.py)

```text
a [5]
b [3]
8.0
```

## Main 3: Return values

[Python solution](main_03.py)

```text
Number [5]
Square: 25.0 Square plus 10: 35.0
```

## Main 4: Default and keyword arguments

[Python solution](main_04.py)

```text
Hello Student
Welcome Asha
Welcome Asha
Positional arguments follow parameter order; keywords identify parameters by name.
```

## Main 5: Built-in functions

[Python solution](main_05.py)

```text
4 10 4 1
String: 6 y P
Manual: 4 10 4 1
sum is numeric; strings are joined using join, not sum.
```

## Main 6: List processing function

[Python solution](main_06.py)

```text
[1, 4, 2] (7, 4)
[10, -2, 8] (16, 10)
[] (0, None)
```

## Main 7: Recursive factorial and trace

[Python solution](main_07.py)

```text
Small nonnegative integer [5]
Call factorial: 5
Call factorial: 4
Call factorial: 3
Call factorial: 2
Call factorial: 1
Return factorial: 2 2
Return factorial: 3 6
Return factorial: 4 24
Return factorial: 5 120
Recursive: 120 Iterative: 120
Both O(n) time; recursion uses O(n) call-stack space, loop O(1) auxiliary space.
```

## Main 8: Recursive Fibonacci

[Python solution](main_08.py)

```text
Number of terms [8]
Recursive: [0, 1, 1, 2, 3, 5, 8, 13]
Iterative: [0, 1, 1, 2, 3, 5, 8, 13]
Naive recursion repeats work exponentially. Memoization gives O(n) work/storage; iteration avoids recursion overhead.
```

## Main 9: Function composition

[Python solution](main_09.py)

```text
Number [5]
Square: 25.0
```

## Main 10: Local and global scope

[Python solution](main_10.py)

```text
Local: 20
Global after local change: 10
Global after global change: 30
```

## Main 11: Function menu

[Python solution](main_11.py)

```text
1. Addition  2. Prime check  3. Factorial
Choice [3]
Number [5]
120
```

## Main 12: Student result functions

[Python solution](main_12.py)

```text
Marks out of 100 [90 80 70]
Total: 240.0/300; percentage: 80.00; grade: B
```

## Practice 1: Average battery drop

[Python solution](practice_01.py)

```text
Average drop per hour: 4.8 percentage points
No warning
```

## Practice 2: BMI function

[Python solution](practice_02.py)

```text
23.51 Normal
```

## Practice 3: Recursive digit sum

[Python solution](practice_03.py)

```text
27
```

## Practice 4: Reusable bill function

[Python solution](practice_04.py)

```text
2655.00
```

## Practice 5: Text sanitizing function

[Python solution](practice_05.py)

```text
('python makes ai easy', 4)
```

## Practice 6: Predict function addition

[Python solution](practice_06.py)

```text
8
```

## Practice 7: Predict default greeting

[Python solution](practice_07.py)

```text
Hello Student
```

## Practice 8: Predict recursive factorial

[Python solution](practice_08.py)

```text
24
```

## Practice 9: Missing colon fix

[Python solution](practice_09.py)

```text
8
```

## Practice 10: Indentation fix

[Python solution](practice_10.py)

```text
25
```
