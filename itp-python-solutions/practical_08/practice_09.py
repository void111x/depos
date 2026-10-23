"""Practical 8 | practice 9: Correct key quoting"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# Unquoted name is a variable lookup and raises NameError if undefined.
student={'name':'Ravi','marks':85}; print(student['name'])
