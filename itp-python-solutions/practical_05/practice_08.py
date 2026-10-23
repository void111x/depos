"""Practical 5 | practice 8: Stop at first defective product"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

products=['OK']*100
products[36]='DEFECTIVE'  # Illustrative first defect at position 37.
for position,status in enumerate(products,1):
    if status=='DEFECTIVE':
        print('Inspection stopped at product',position)
        break
    print('Passed',position)
else: print('All products passed')
