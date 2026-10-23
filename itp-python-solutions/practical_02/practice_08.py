"""Practical 2 | practice 8: Verify precedence"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

print('Predicted outputs: 20, 30, 26.0, 47.0, 16')
print(10+5*2,(10+5)*2,100/5+3*2,50-6/2,8+2**3)
print('Parentheses, exponentiation, multiplication/division, addition/subtraction.')
