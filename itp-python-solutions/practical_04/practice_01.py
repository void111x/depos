"""Practical 4 | practice 1: Range endpoint correction"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# Stop is exclusive: 11 is needed to include 10.
for i in range(1,11): print(i)
