"""Practical 4 | main 8: Prime checker"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

from math import isqrt
n=int(ask('Integer',29)); prime=n>=2
if prime:
    for divisor in range(2,isqrt(n)+1):
        if n%divisor==0:
            prime=False
            break
print('Prime' if prime else 'Not prime')
print('Only test divisors up to the square root.')
