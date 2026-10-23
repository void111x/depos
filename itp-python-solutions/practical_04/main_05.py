"""Practical 4 | main 5: Multiplication table"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

n=int(ask('Number',7))
for i in range(1,11): print(f'{n} x {i} = {n*i}')
