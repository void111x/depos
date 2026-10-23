"""Practical 7 | practice 7: Meal price sorting"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

meals=[['Veg Burger',120],['Pizza Slice',90],['Pasta Bowl',150],['Sandwich',80]]
meals.append(['Noodles',110]); meals.sort(key=lambda meal:meal[1]); print(meals)
