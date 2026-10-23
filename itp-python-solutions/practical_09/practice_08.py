"""Practical 9 | practice 8: Predict recursive factorial"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def fact(n):
    if n==1: return 1
    return n*fact(n-1)
print(fact(4))  # Original snippet assumes a positive integer.
