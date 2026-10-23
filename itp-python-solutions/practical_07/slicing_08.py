"""Practical 7 | slicing 8: Middle submatrix"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.arange(1,17).reshape(4,4)
print(a[1:3,1:3])
print('NumPy slices both axes in one expression; basic slices usually share data with the original array.')
