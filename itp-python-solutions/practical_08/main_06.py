"""Practical 8 | main 6: Dictionary iteration"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

d={'a':1,'b':2}
for key in d: print('Key:',key)
for value in d.values(): print('Value:',value)
for key,value in d.items(): print(key,value)
