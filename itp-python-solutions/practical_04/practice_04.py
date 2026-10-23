"""Practical 4 | practice 4: Fix Fibonacci update"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# Sequential a=b; b=a+b loses the old a. Update simultaneously.
a,b=0,1
for i in range(5):
    print(a)
    a,b=b,a+b
