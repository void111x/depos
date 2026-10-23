"""Practical 8 | main 12: Inventory operations"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

inventory={'Pen':10,'Book':5}; inventory['Pencil']=20; inventory['Pen']+=5; inventory.pop('Book'); print(inventory)
