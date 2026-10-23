"""Practical 2 | practice 5: Fuel cost"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

distance,mileage,price=240,15,105
litres=distance/mileage
print(f'Fuel: {litres:.2f} litres; cost: Rs {litres*price:.2f}')
