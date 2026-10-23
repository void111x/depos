"""Practical 8 | main 11: Sort dictionary"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

d={'banana':3,'apple':5,'orange':2}
print('By key:',dict(sorted(d.items())))
print('By value:',dict(sorted(d.items(),key=lambda pair:pair[1])))
