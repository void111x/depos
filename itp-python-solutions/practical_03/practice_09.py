"""Practical 3 | practice 9: Systolic classification exercise"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

systolic=float(ask('Systolic reading',125))
if systolic<=0: raise ValueError('Reading must be positive')
# Assumed worksheet thresholds, based only on systolic; not a diagnosis.
if systolic<120: print('Normal')
elif systolic<130: print('Elevated')
elif systolic<140: print('High Stage 1')
else: print('High Stage 2')
