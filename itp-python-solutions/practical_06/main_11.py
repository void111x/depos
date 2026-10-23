"""Practical 6 | main 11: Matrix multiplication"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([[1,2],[3,4]]); b=np.array([[5,6],[7,8]])
manual=[[sum(int(a[i,k])*int(b[k,j]) for k in range(a.shape[1])) for j in range(b.shape[1])] for i in range(a.shape[0])]
print('A @ B:',a@b); print('Transpose:',a.T); print('Manual:',manual)
print('Equal:',np.array_equal(a@b,manual))
