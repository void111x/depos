"""Practical 2 | main 4: Precedence"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

print('Predicted: 20, 30, 26.0')
print(10+5*2, (10+5)*2, 100/5+3*2)
print('Parentheses first, then multiplication/division, then addition/subtraction.')
