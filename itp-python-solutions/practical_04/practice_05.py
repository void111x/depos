"""Practical 4 | practice 5: Fix infinite loop"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

num=1
while num<=5:
    print(num)
    num+=1  # Missing update caused the infinite loop.
