"""Practical 5 | main 6: Print positive values"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

numbers=list(map(float,ask('Numbers','-2 0 4 -1 9').split()))
for n in numbers:
    if n<0: continue
    if n>0: print(n)  # Zero is not positive.
