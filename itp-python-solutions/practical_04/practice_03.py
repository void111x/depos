"""Practical 4 | practice 3: Fix nested indentation"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# Literal corrected snippet prints nine stars on separate lines.
for i in range(3):
    for j in range(3):
        print('*')
print('Optional 3 x 3 layout:')
for i in range(3):
    for j in range(3): print('*',end='')
    print()
