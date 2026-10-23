"""Practical 3 | main 8: Discount thresholds"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

amount=float(ask('Purchase amount',2000))
if amount<0: raise ValueError('Amount must be nonnegative')
# Worksheet omits comparison signs: interpret thresholds as at least.
if amount>=2000: rate=.2
elif amount>=1000: rate=.1
else: rate=0
print(f'Discount: {amount*rate:.2f}; payable: {amount*(1-rate):.2f}')
