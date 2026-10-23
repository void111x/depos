"""Practical 6 | main 8: Elementwise array arithmetic"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([1,2,3]); b=np.array([4,5,6])
print(a+b,a-b,a*b)
x,y=a.tolist(),b.tolist()
print('Lists concatenate with +:',x+y)
print('Manual elementwise:',[u+v for u,v in zip(x,y)],[u-v for u,v in zip(x,y)],[u*v for u,v in zip(x,y)])
