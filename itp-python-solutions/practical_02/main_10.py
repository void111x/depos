"""Practical 2 | main 10: Error handling"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

try:
    print(10/0)
except ZeroDivisionError:
    print('ZeroDivisionError: denominator must not be zero.')
try:
    print('10'+5)
except TypeError:
    print('TypeError: convert the string to a number.')
denominator = float(ask('Denominator',2))
print(10/denominator if denominator else 'Division prevented')
print(int('10')+5)
