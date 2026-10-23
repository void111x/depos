"""Practical 3 | practice 5: Parking charges"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

from math import ceil
hours=float(ask('Hours parked (one day)',4))
if not 0<=hours<=24: raise ValueError('Enter hours from 0 to 24')
# Assumption: each started hour is charged; zero hours costs zero.
charge=0 if hours==0 else min(100,20+10*(ceil(hours)-1))
print(f'Parking charge: Rs {charge:.2f}')
