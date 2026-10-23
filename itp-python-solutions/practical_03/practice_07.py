"""Practical 3 | practice 7: Scholarship eligibility"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

marks=float(ask('Marks',86)); income=float(ask('Family income',299999))
print('Eligible' if marks>85 and income<300000 else 'Not eligible')
