"""Practical 10 | main 2: Basic slices"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text='PythonProgramming'
print(text[:5],text[-4:],text[2:7])
print('[start:end] includes start and excludes end; indices 2 through 7 inclusive would be [2:8].')
