"""Practical 3 | practice 1: Placement eligibility"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

cgpa=float(ask('CGPA',7)); attendance=float(ask('Attendance percent',75))
print('Eligible' if cgpa>=7 and attendance>=75 else 'Not eligible')
