"""Practical 5 | practice 1: Drone low battery"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# Illustrative stream: worksheet supplies no readings.
for row,battery in enumerate([90,65,30,15,14,10],1):
    if battery<15:
        print('Stopped before row',row,'battery:',battery)
        break
    print('Scanning row',row)
