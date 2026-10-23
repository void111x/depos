"""Practical 2 | practice 4: Arithmetic comparisons"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a,b=25,4
for label,value in [('a+b',a+b),('a-b',a-b),('a*b',a*b),('a/b',a/b),('a//b',a//b),('a%b',a%b),('a**b',a**b)]:
    print(label,'=',value)
print('/ gives true division; // floors the quotient; % gives the remainder; ** gives power.')
