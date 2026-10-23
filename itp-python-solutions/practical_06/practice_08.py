"""Practical 6 | practice 8: Weighted revenue"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
sales=np.array([[100,120,130,140,150],[110,125,135,145,155],[90,100,110,120,130],[80,95,105,115,125],[70,85,95,105,115],[60,75,85,95,105],[50,65,75,85,95]])
weights=np.array([2,3,1,4,5])
print('Weighted revenue per store:',sales@weights)
