"""Practical 4 | practice 10: Predict star pattern"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

for i in range(3):
    for j in range(i+1): print('*',end='')
    print()
