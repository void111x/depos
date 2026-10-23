"""Practical 1 | main 3: Constants by convention"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

PI, GRAVITY, MAX_USERS = 3.14159, 9.81, 100
print(PI, GRAVITY, MAX_USERS)
PI = 3.14
print('Reassignment is allowed:', PI)
print('UPPER_CASE names communicate constants; Python does not enforce them. Avoid reassignment by convention.')
