"""Practical 3 | main 4: Nested voting check"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

age=int(ask('Age',18)); nationality=ask('Nationality','Indian').strip().lower()
if age>=18:
    if nationality=='indian': print('Eligible')
    else: print('Not eligible: nationality')
else: print('Not eligible: age')
