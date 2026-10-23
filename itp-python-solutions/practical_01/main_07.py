"""Practical 1 | main 7: Identity and mutability"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a = b = 10
print('Before:', id(a), id(b))
a += 1
print('After:', id(a), id(b), a, b)
x = y = [1, 2]
x.append(3)
print('Shared mutable list:', x, y, id(x) == id(y))
print('Integers are immutable; rebinding a does not change b. id values vary by run.')
