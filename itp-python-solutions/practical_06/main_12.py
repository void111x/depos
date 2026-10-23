"""Practical 6 | main 12: Student marks analysis"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
marks=np.array([[80,90,85],[70,75,80],[95,88,92]])
print('Per-student averages:',marks.mean(axis=1))
print('Highest:',marks.max(),'Lowest:',marks.min())
