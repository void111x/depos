"""Practical 9 | practice 9: Missing colon fix"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def add(a,b):  # A function header ends in a colon.
    return a+b
print(add(5,3))
