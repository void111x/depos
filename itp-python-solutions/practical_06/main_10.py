"""Practical 6 | main 10: Reshaping constraints"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.arange(12)
print(a.reshape(3,4)); print(a.reshape(2,6))
try: print(a.reshape(5,3))
except ValueError: print('New dimensions must multiply to the original element count (12).')
