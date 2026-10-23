"""Practical 6 | practice 10: Terrain grid"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
rng=np.random.default_rng(42)
a=rng.integers(100,501,size=(10,10))
print(a)
print('Highest:',a.max(),'Indices:',np.argwhere(a==a.max()))
print('Lowest:',a.min(),'Indices:',np.argwhere(a==a.min()))
print('Mean:',a.mean(),'Central 4 x 4:',a[3:7,3:7])
