"""Practical 1 | practice 5: Decimal string conversion"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# int('12.5') raises ValueError. Use float, or int(float(...)) to truncate.
num = float('12.5')
print(num)
print('Truncated integer:', int(num))
