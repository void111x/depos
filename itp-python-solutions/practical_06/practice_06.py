"""Practical 6 | practice 6: Traffic reshape"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([120,135,140,150,160,155,148,170,180,175,190,200,210,205,198,220,230,225,240,250,245,238,230,220]).reshape(3,8)
print(a)
print('Peak count:',a.max(),'Junction/slot:',np.argwhere(a==a.max())+1)
rows=a.sum(axis=1)
print('Least busy junction:',np.flatnonzero(rows==rows.min())+1,'Average:',a.mean())
print('Only 24 values supplied: use requested 3 x 8 reshape, not 3 x 24.')
