"""Practical 4 | main 6: Reverse and palindrome"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

n=int(ask('Nonnegative integer',1221))
if n<0: raise ValueError('Use a nonnegative integer')
original=n; reverse=0
while n:
    reverse=reverse*10+n%10
    n//=10
print('Reverse:',reverse,'Palindrome:',original==reverse)
