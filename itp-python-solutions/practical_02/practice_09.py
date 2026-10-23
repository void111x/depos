"""Practical 2 | practice 9: Split restaurant bill"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

bill,friends,tip_rate=1800,4,8
tip=bill*tip_rate/100; final=bill+tip
print(f'Tip: {tip:.2f}; final: {final:.2f}; per friend: {final/friends:.2f}')
