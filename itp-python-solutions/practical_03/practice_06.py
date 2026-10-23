"""Practical 3 | practice 6: Age categories"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

age=int(ask('Age',18))
# Assumed ranges: child 0-12, teen 13-19, adult 20-59, senior 60+.
if age<0: raise ValueError('Age must be nonnegative')
if age<13: print('Child')
elif age<20: print('Teen')
elif age<60: print('Adult')
else: print('Senior Citizen')
