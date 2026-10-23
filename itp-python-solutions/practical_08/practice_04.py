"""Practical 8 | practice 4: Retail inventory"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

inventory={'Laptop':12,'Mouse':40,'Keyboard':25,'Monitor':10}
inventory['Laptop']-=2; inventory['Printer']=5
for product in list(inventory):
    if inventory[product]==0: del inventory[product]
print(inventory)  # This dataset has no zero-stock products.
