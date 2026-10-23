"""Practical 1 | main 2: Dynamic typing"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

x = 10
print(x, type(x))
x = 'Python'
print(x, type(x))
x = 3.5
print(x, type(x))
print('Python names can refer to different types; statically typed variables have a declared or inferred fixed type.')
