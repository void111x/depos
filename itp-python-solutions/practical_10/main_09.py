"""Practical 10 | main 9: Strip replace format"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text='  Python is fun  '; clean=text.strip(); changed=clean.replace('fun','powerful')
print(f'Original: {text!r}; stripped: {clean!r}; replaced: {changed}')
