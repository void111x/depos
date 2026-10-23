"""Practical 7 | main 1: Lists and tuples"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

numbers=[1,2,3]; words=('red','green','blue')
print(numbers,type(numbers)); print(words,type(words))
print('Lists use []; tuples use commas, usually inside ().')
