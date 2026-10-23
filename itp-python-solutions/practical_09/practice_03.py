"""Practical 9 | practice 3: Recursive digit sum"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def digit_sum(n):
    n=abs(n)
    if n<10: return n
    return n%10+digit_sum(n//10)
print(digit_sum(482931))
