"""Practical 8 | practice 1: Attendance updates"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

attendance={'S101':'Present','S102':'Absent','S103':'Present','S104':'Late'}
attendance['S104']='Present'; attendance['S105']='Present'
print(attendance); print('Present:',sum(status=='Present' for status in attendance.values()))
