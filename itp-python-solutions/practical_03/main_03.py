"""Practical 3 | main 3: Grade using elif"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

m=float(ask('Marks',85))
if not 0<=m<=100: raise ValueError('Marks must be 0 to 100')
if m>=90: print('A')
elif m>=75: print('B')
elif m>=50: print('C')
else: print('Fail')
