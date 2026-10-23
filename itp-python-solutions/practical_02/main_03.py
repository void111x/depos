"""Practical 2 | main 3: Expressions"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a,b,c = [float(ask(name, value)) for name,value in zip(('a','b','c'),(10,20,3))]
print('Sum:',a+b+c,'Average:',(a+b+c)/3,'Expression:',(a+b)*c/2)
