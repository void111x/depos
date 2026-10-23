"""Practical 3 | practice 3: Shopping discount"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

amount=float(ask('Purchase',5000))
if amount<0: raise ValueError('Amount must be nonnegative')
if amount>5000: rate=.15
elif amount>2000: rate=.10
else: rate=0
print(f'Discount: {amount*rate:.2f}; final: {amount*(1-rate):.2f}')
