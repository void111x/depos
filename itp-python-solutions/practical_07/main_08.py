"""Practical 7 | main 8: Tuple count and index"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

values=(2,3,2,4)
print('Count of 2:',values.count(2),'Index of 4:',values.index(4))
try: print(values.index(9))
except ValueError: print('Missing element: index raises ValueError; count returns',values.count(9))
