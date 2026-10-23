"""Practical 7 | main 7: Sort and reverse"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

items=[3,1,4,2]; items.sort(); print('Ascending:',items)
items.sort(reverse=True); print('Descending:',items)
items.reverse(); print('Reversed current order:',items)
print('reverse flips the existing order; sort orders by value.')
