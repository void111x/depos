"""Practical 1 | main 10: Boolean conditions"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

age, marks = int(ask('Age', 19)), float(ask('Marks', 75))
is_adult, is_pass = age > 18, marks > 50
print(is_adult, is_pass)
if is_adult and is_pass:
    print('Both worksheet conditions satisfied.')
else:
    print('At least one condition is not satisfied.')
