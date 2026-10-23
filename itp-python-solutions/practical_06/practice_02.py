"""Practical 6 | practice 2: ICU temperature matrix"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([[98.6,99.1,100.2,99.8,98.9,99.0],[97.8,98.0,98.4,98.6,98.2,98.1],[101.2,100.8,101.5,102.0,101.7,101.3],[99.4,99.5,99.6,99.3,99.2,99.1],[98.7,98.9,99.0,98.8,98.6,98.5]])
print('Per-patient maxima:',a.max(axis=1))
print('Per-patient averages:',a.mean(axis=1),'Overall average:',a.mean())
indices=np.flatnonzero(a.max(axis=1)==a.max())
print('Highest-temperature patient indices:',indices,'Patient numbers:',indices+1)
print('Worksheet labels C but values resemble F. Values retained unchanged; critical interpreted as highest temperature, no clinical threshold given.')
