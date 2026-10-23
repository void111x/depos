"""Practical 6 | practice 9: Rainfall halves"""

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
a=rng.integers(20,121,size=(8,30))
first,last=a[:,:15],a[:,15:]
print('First 15 days:',first); print('Last 15 days:',last)
print('District averages first:',first.mean(axis=1),'last:',last.mean(axis=1))
print('Overall first:',first.mean(),'last:',last.mean(),'Change:',last.mean()-first.mean())
