"""Practical 5 | practice 6: Sensor average"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

readings=[22,24,-1,26,-5,28]; total=count=0
for value in readings:
    if value<0: continue  # This worksheet defines negatives as faulty.
    total+=value; count+=1
print('Average:',total/count if count else 'No valid readings')
