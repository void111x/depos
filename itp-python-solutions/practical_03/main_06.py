"""Practical 3 | main 6: Leap year"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

year=int(ask('Year',2024))
print('Leap year' if year%400==0 or (year%4==0 and year%100!=0) else 'Not leap year')
