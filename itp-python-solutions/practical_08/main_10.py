"""Practical 8 | main 10: Merge dictionaries"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a={'x':1,'y':2}; b={'y':20,'z':3}; a.update(b); print(a)
print('The incoming value overwrites an existing matching key.')
