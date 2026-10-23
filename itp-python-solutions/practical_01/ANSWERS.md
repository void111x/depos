# Practical 1: solutions and sample outputs

Run each linked Python file with `--demo` to reproduce the samples. Omit `--demo` to enter your own inputs where requested. Comments in each program explain corrections and assumptions.

## Main 1: Variables and naming rules

[Python solution](main_01.py)

```text
Ishaan 18 85.5 Mumbai
1name = "Python" -> SyntaxError: invalid decimal literal
class = 1 -> SyntaxError: invalid syntax
my-name = 1 -> SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
Names cannot start with digits, use keywords, or contain hyphens.
```

## Main 2: Dynamic typing

[Python solution](main_02.py)

```text
10 <class 'int'>
Python <class 'str'>
3.5 <class 'float'>
Python names can refer to different types; statically typed variables have a declared or inferred fixed type.
```

## Main 3: Constants by convention

[Python solution](main_03.py)

```text
3.14159 9.81 100
Reassignment is allowed: 3.14
UPPER_CASE names communicate constants; Python does not enforce them. Avoid reassignment by convention.
```

## Main 4: Data type identification

[Python solution](main_04.py)

```text
Integer [10]
Float [3.5]
String [Python]
Boolean true/false [true]
Value               Type
10                  int
3.5                 float
Python              str
True                bool
```

## Main 5: Explicit casting

[Python solution](main_05.py)

```text
Age [18]
Marks [85.5]
Age next year: 19 Marks plus 5: 90.5
TypeError: input is a string; convert before numeric addition.
Without conversion, + joins strings: 181
```

## Main 6: Implicit and explicit conversion

[Python solution](main_06.py)

```text
12.5 <class 'float'>
int + str raises TypeError: no automatic string-to-number conversion.
15
int + float promotes the numeric result to float.
```

## Main 7: Identity and mutability

[Python solution](main_07.py)

```text
Before: 22317816 22317816
After: 22317848 22317816 11 10
Shared mutable list: [1, 2, 3] [1, 2, 3] True
Integers are immutable; rebinding a does not change b. id values vary by run.
```

## Main 8: Two swap methods

[Python solution](main_08.py)

```text
Temporary variable: 20 10
Tuple unpacking: 20 10
Both swap values; unpacking is shorter.
```

## Main 9: Type-based calculator

[Python solution](main_09.py)

```text
First value [12]
Second value [3.5]
Types: int float
15.5
```

## Main 10: Boolean conditions

[Python solution](main_10.py)

```text
Age [19]
Marks [75]
True True
Both worksheet conditions satisfied.
```

## Main 11: Temperature conversion

[Python solution](main_11.py)

```text
Celsius [37]
37.00 C = 98.60 F
```

## Practice 1: Invalid identifier

[Python solution](practice_01.py)

```text
Python
```

## Practice 2: String plus integer

[Python solution](practice_02.py)

```text
23
```

## Practice 3: Undefined name

[Python solution](practice_03.py)

```text
95
```

## Practice 4: Boolean capitalization

[Python solution](practice_04.py)

```text
True
```

## Practice 5: Decimal string conversion

[Python solution](practice_05.py)

```text
12.5
Truncated integer: 12
```

## Practice 6: Predict dynamic type

[Python solution](practice_06.py)

```text
<class 'str'>
```

## Practice 7: Predict addition

[Python solution](practice_07.py)

```text
25
```

## Practice 8: Predict swap

[Python solution](practice_08.py)

```text
20 10
```

## Practice 9: Predict Boolean

[Python solution](practice_09.py)

```text
True
```

## Practice 10: Predict Fahrenheit

[Python solution](practice_10.py)

```text
98.6
```
