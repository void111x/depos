"""Practical 5 | main 5: First divisible number"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

n=int(ask('Divisor',7))
if n==0: raise ValueError('Divisor cannot be zero')
for value in range(1,101):
    if value%n==0:
        print(value)
        break
else: print('No multiple in 1 to 100')
