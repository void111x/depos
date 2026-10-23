"""Practical 5 | practice 4: Skip damaged barcode"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

for barcode in [101,102,-1,104,-1,106]:
    if barcode==-1: continue
    print('Scanned',barcode)
