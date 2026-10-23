"""Practical 6 | practice 1: Soil moisture"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import numpy as np
a=np.array([[45,50,48,52,47,49,51],[55,53,54,52,56,57,55],[38,40,42,39,41,43,44],[60,62,61,63,64,62,65]])
print('Zone averages:',a.mean(axis=1))
# Interpret highest/lowest day by the average across zones; also show each zone.
daily=a.mean(axis=0)
print('Daily averages:',daily)
print('Highest days:',np.flatnonzero(daily==daily.max())+1,'Lowest days:',np.flatnonzero(daily==daily.min())+1)
for i,row in enumerate(a,1):
    print('Zone',i,'highest days',np.flatnonzero(row==row.max())+1,'lowest days',np.flatnonzero(row==row.min())+1)
