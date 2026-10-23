"""Practical 3 | practice 8: Recharge benefits"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

amount=int(ask('Recharge rupees',299))
if amount<0: raise ValueError('Amount must be nonnegative')
if amount>=299: print('2 GB/day')
elif amount>=199: print('1 GB/day')
else: print('Talktime only')
