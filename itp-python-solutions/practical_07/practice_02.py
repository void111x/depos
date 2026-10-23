"""Practical 7 | practice 2: Drone coordinates"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

points=[(10,20,150),(15,25,160),(20,30,170),(25,35,180),(30,40,190),(35,45,200),(40,50,210),(45,55,220),(50,60,230),(55,65,240)]
for x,y,z in points: print('x:',x,'y:',y,'altitude:',z)
