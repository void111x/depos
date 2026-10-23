"""Practical 6 | main 9: Array statistics"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([10,20,30,40,50])
print('Mean:',a.mean(),'Median:',np.median(a),'Population SD:',a.std(ddof=0))
