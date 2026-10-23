"""Practical 10 | main 3: Stepped slices"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text='PythonProgramming'; print('Alternate:',text[::2]); print('Reverse:',text[::-1])
print('Step 2 takes every other character; step -1 traverses backwards.')
