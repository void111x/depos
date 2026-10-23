"""Practical 6 | main 7: NumPy indexing and slicing"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.arange(1,13).reshape(3,4)
print(a); print('Element [1,2]:',a[1,2]); print('Row:',a[1,:]); print('Column:',a[:,2]); print('Slice:',a[:2,1:3])
