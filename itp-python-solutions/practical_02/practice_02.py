"""Practical 2 | practice 2: Average speed"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

distance,time=float(ask('Distance km',180)),float(ask('Time hours',3))
if distance<0 or time<=0: raise ValueError('Distance >= 0 and time > 0 required')
print(f'Average speed: {distance/time:.2f} km/h')
