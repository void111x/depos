"""Practical 2 | main 8: Single-line input"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a,b,c = map(float, ask('Three numbers separated by spaces','2 3 4').split())
print(f'Sum: {a+b+c}; product: {a*b*c}')
