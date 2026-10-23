"""Practical 8 | practice 10: Correct dictionary update"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# Dictionaries have no append method; use update or assign a key.
d={'a':1,'b':2}; d.update({'c':3}); print(d)
