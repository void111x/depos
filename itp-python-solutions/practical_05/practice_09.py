"""Practical 5 | practice 9: Skip weekends over 30 days"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# Assume day 1 is Monday. Index 5=Saturday, 6=Sunday.
for day in range(1,31):
    weekday=(day-1)%7
    if weekday in (5,6): continue
    print('Analyze day',day)
