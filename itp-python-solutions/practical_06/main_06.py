"""Practical 6 | main 6: NumPy creation"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
for a in (np.array([[1,2],[3,4]]),np.zeros((2,3)),np.ones((3,2))):
    print(a); print('Shape:',a.shape,'dtype:',a.dtype)
