"""Practical 9 | main 11: Function menu"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

from math import isqrt
def add(a,b): return a+b
def is_prime(n):
    if n<2: return False
    for d in range(2,isqrt(n)+1):
        if n%d==0: return False
    return True
def factorial(n):
    if n<0: raise ValueError('Nonnegative integer required')
    result=1
    for i in range(2,n+1): result*=i
    return result
print('1. Addition  2. Prime check  3. Factorial')
choice=ask('Choice',3)
if choice=='1': print(add(float(ask('a',5)),float(ask('b',3))))
elif choice=='2': print(is_prime(int(ask('Number',29))))
elif choice=='3': print(factorial(int(ask('Number',5))))
else: print('Invalid choice')
