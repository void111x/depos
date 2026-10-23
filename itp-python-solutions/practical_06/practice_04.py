"""Practical 6 | practice 4: Brightness inversion"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([[120,135,140,150,160,170],[110,125,130,145,155,165],[100,115,120,135,145,155],[90,105,110,125,135,145],[80,95,100,115,125,135],[70,85,90,105,115,125]])
print(255-a)
