"""Practical 3 | main 9: Triangle types"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a,b,c=map(float,ask('Three sides','3 4 5').split())
if min(a,b,c)<=0 or a+b<=c or a+c<=b or b+c<=a: print('Invalid triangle')
elif a==b==c: print('Equilateral')
elif a==b or b==c or a==c: print('Isosceles')
else: print('Scalene')
