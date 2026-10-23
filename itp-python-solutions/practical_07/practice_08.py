"""Practical 7 | practice 8: GPS route slices"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

points=[(18.5204,73.8567),(18.5210,73.8575),(18.5221,73.8580),(18.5232,73.8591),(18.5243,73.8602),(18.5254,73.8613),(18.5265,73.8624),(18.5276,73.8635),(18.5287,73.8646),(18.5298,73.8657)]
print('Alternate:',points[::2]); print('First five:',points[:5]); print('Reverse:',points[::-1])
print('Worksheet says 20 points but supplies 10; all 10 supplied points used.')
