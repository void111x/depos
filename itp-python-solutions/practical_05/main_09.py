"""Practical 5 | main 9: Pass placeholder"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

for n in range(3):
    if n==1:
        pass  # A syntactically valid empty block; execution continues.
    print(n)
print('pass does nothing; it is not continue.')
