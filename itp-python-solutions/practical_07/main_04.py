"""Practical 7 | main 4: Mutability"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

numbers=[1,2,3]; fixed=(1,2,3)
numbers[0]=9; print(numbers)
try: fixed[0]=9
except TypeError: print('Tuples do not support item assignment.')
