"""Practical 4 | main 9: Fibonacci iteration"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

n=int(ask('Terms',8))
if n<0: raise ValueError('Count must be nonnegative')
a,b=0,1
for _ in range(n):
    print(a,end=' ')
    a,b=b,a+b
print('\nUpdate both values using their old values.')
