"""Practical 2 | main 6: Area and perimeter"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

from math import pi
length,width,radius = [float(ask(n,v)) for n,v in [('Length',5),('Width',3),('Radius',2)]]
if min(length,width,radius)<0: raise ValueError('Dimensions must be nonnegative')
print(f'Rectangle area: {length*width:.2f}; perimeter: {2*(length+width):.2f}')
print(f'Circle area: {pi*radius**2:.2f}; circumference: {2*pi*radius:.2f}')
