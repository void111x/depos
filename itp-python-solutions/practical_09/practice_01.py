"""Practical 9 | practice 1: Average battery drop"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def average_drop(readings):
    if len(readings)<2: raise ValueError('At least two readings required')
    return sum(readings[i-1]-readings[i] for i in range(1,len(readings)))/(len(readings)-1)
drop=average_drop([92,88,84,79,73,68])
print('Average drop per hour:',drop,'percentage points')
print('Warning' if drop>5 else 'No warning')
# Six hourly readings contain five elapsed intervals; do not divide by six.
