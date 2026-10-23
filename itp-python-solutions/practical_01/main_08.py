"""Practical 1 | main 8: Two swap methods"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a, b = 10, 20
temp = a
a = b
b = temp
print('Temporary variable:', a, b)
a, b = 10, 20
a, b = b, a
print('Tuple unpacking:', a, b)
print('Both swap values; unpacking is shorter.')
