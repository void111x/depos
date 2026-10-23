"""Practical 3 | main 7: Conditional calculator"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a,b=float(ask('a',10)),float(ask('b',2)); op=ask('Operator','/')
if op=='+': print(a+b)
elif op=='-': print(a-b)
elif op=='*': print(a*b)
elif op=='/': print(a/b if b else 'Cannot divide by zero')
else: print('Invalid operator')
