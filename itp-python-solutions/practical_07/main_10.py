"""Practical 7 | main 10: List and tuple conversion"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

items=[1,2,3]; fixed=tuple(items); editable=list(fixed); editable[0]=9
print('Tuple:',fixed,'Modified list:',editable)
