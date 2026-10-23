"""Practical 7 | main 11: Sequence iteration"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

numbers=[1,2,3]; fixed=tuple(numbers)
for data in (numbers,fixed):
    total=0
    for value in data:
        print(value); total+=value
    print(type(data).__name__,'sum:',total)
