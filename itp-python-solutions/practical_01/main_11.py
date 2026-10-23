"""Practical 1 | main 11: Temperature conversion"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

c = float(ask('Celsius', 37))
print(f'{c:.2f} C = {c * 9 / 5 + 32:.2f} F')
