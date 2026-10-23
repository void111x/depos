"""Practical 8 | main 3: Get with default"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

student={'name':'Asha','marks':92}
print(student.get('name')); print(student.get('city','Not provided'))
print('get returns the default for an absent key; indexing raises KeyError.')
