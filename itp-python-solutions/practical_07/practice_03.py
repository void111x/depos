"""Practical 7 | practice 3: Doctor shifts"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

shifts=[['Dr A','Dr B','Dr C'],['Dr D','Dr E','Dr F'],['Dr G','Dr H','Dr I'],['Dr J','Dr K','Dr L'],['Dr M','Dr N','Dr O'],['Dr P','Dr Q','Dr R'],['Dr S','Dr T','Dr U']]
shifts[4][2]='Dr Z'  # Day 5, third/night shift.
for day,row in enumerate(shifts,1): print(day,row)
