"""Practical 7 | slicing 7: NumPy row and column slices"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.arange(1,10).reshape(3,3)
print(a[:2,:]); print(a[:,-1])
m=a.tolist(); print(m[:2]); print([row[-1] for row in m])
