"""Practical 6 | practice 3: Room occupancy"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([[1,1,0,1,0,1,1,0],[1,0,1,1,1,0,1,1],[0,1,1,0,1,1,0,1],[1,1,1,1,0,0,1,0],[0,0,1,1,1,1,1,1]])
counts=a.sum(axis=1)
print('Busiest rooms:',np.flatnonzero(counts==counts.max())+1)
print('Free slots:',np.count_nonzero(a==0),'Occupancy:',100*a.mean(),'%')
