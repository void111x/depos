"""Practical 5 | main 10: Nested skipping pattern"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

for row in range(1,6):
    for value in range(1,row+1):
        if value%2==0: continue
        print(value,end=' ')
    print()
