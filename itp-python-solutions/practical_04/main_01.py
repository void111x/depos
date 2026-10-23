"""Practical 4 | main 1: For loop and range"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

for i in range(1,11): print(i,end=' ')
print()
for i in range(2,11,2): print(i,end=' ')
print('\nrange includes start, excludes stop, advances by step.')
