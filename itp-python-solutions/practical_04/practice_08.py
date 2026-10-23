"""Practical 4 | practice 8: Fix factorial initialization"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# Multiplication must start at 1, not 0.
n=5; fact=1
for i in range(1,n+1): fact*=i
print(fact)
