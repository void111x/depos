"""Practical 2 | main 1: Input and output"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

name, age = ask('Name', 'Ishaan'), int(ask('Age', 18))
print('Name:', name, 'Age:', age)
print(f'Name: {name} Age: {age}')
print('Both display the same information; f-strings embed expressions in text.')
