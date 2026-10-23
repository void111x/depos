"""Practical 9 | practice 4: Reusable bill function"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def bill_amount(price,discount,gst):
    if price<0 or not 0<=discount<=100 or gst<0: raise ValueError('Invalid price or percentage')
    return price*(1-discount/100)*(1+gst/100)
print(f'{bill_amount(2500,10,18):.2f}')
