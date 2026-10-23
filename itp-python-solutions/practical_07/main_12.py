"""Practical 7 | main 12: Shopping cart"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

categories=('Food','Stationery','Electronics'); cart=['Bread','Pen']
cart.append('Milk'); cart.remove('Pen')
print('Categories:',categories,'Cart:',cart,'Item count:',len(cart))
