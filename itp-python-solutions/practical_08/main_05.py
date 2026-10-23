"""Practical 8 | main 5: Remove dictionary entries"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

d={'a':1,'b':2,'c':3}; print('Popped:',d.pop('a')); del d['b']; print(d)
try: del d['missing']
except KeyError: print('del on missing key raises KeyError.')
try: d.pop('missing')
except KeyError: print('pop without a default also raises KeyError.')
print(d.pop('missing','Safe default'))
