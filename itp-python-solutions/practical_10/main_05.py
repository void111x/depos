"""Practical 10 | main 5: Membership"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text='Python makes coding easy'; word=ask('Substring','coding')
if word in text: print('Found')
if word not in text: print('Not found')
