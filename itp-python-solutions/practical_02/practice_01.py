"""Practical 2 | practice 1: Electricity bill"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

units=float(ask('Units consumed',150))
if units<0: raise ValueError('Units must be nonnegative')
fixed=150; variable=max(0,units-100)*6
print(f'Fixed: {fixed:.2f}; variable: {variable:.2f}; payable: {fixed+variable:.2f}')
