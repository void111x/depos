"""Practical 7 | practice 5: Calibration tuple replacement"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

points=[(0,0),(10,5),(20,10),(30,15),(40,20)]
try: points[2][0]=25
except TypeError: print('Cannot modify a tuple element; replace the whole tuple in the mutable outer list.')
points[2]=(25,12); print(points)
