"""Practical 6 | practice 7: Heart rate reshape"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([72,74,73,75,76,74,73,72,78,80,82,79,77,76,75,74,73,72,71,70,69,68,67,66,72,74,76,78,80,82,84,83,81,79,77,75,74,73,72,71,70,69,68,67,66,65,72,74,76,78,80,82,84,86,88,85,83,81,79,77])
print(a.reshape(12,5))
