"""Practical 8 | main 7: Views as lists"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

d={'a':1,'b':2}
print(list(d.keys()),list(d.values()),list(d.items()))
