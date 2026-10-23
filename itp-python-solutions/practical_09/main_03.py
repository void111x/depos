"""Practical 9 | main 3: Return values"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def square(number):
    return number*number
result=square(float(ask('Number',5))); print('Square:',result,'Square plus 10:',result+10)
