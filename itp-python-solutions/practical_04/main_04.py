"""Practical 4 | main 4: Factorial with two loops"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

n=int(ask('Nonnegative integer',5))
if n<0: raise ValueError('Factorial requires n >= 0')
a=1
for i in range(1,n+1): a*=i
b=1; i=1
while i<=n:
    b*=i
    i+=1
print('for:',a,'while:',b)
print('Both accumulate the same product; while updates its counter explicitly.')
