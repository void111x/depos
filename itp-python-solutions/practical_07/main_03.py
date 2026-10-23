"""Practical 7 | main 3: List and tuple slices"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

for data in ([1,2,3,4,5],(1,2,3,4,5)):
    print(data[:3],data[-2:],data[::2])
print('Slices preserve the original sequence type; stop is exclusive.')
