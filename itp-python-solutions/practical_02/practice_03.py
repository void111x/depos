"""Practical 2 | practice 3: Discount and GST"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

price,discount_rate,gst_rate=2500,10,18
discount=price*discount_rate/100; taxable=price-discount; gst=taxable*gst_rate/100
print(f'Discount: {discount:.2f}; GST: {gst:.2f}; net bill: {taxable+gst:.2f}')
