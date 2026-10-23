"""Practical 6 | practice 5: Warehouse stocks"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([[10,12,15,18,20,16,14,13,11,9],[8,10,12,14,16,18,20,22,24,26],[5,7,9,11,13,15,17,19,21,23],[30,28,26,24,22,20,18,16,14,12]])
rows=a.sum(axis=1)
print('Busiest shelf (largest stock):',np.flatnonzero(rows==rows.max())+1)
print('Max stock:',a.max(),'Shelf/bin positions:',np.argwhere(a==a.max())+1)
print('Row totals:',rows,'Column totals:',a.sum(axis=0))
