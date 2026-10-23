"""Practical 9 | main 4: Default and keyword arguments"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def greet(name='Student',message='Hello'):
    print(message,name)
greet(); greet('Asha','Welcome'); greet(message='Welcome',name='Asha')
print('Positional arguments follow parameter order; keywords identify parameters by name.')
