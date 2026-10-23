"""Practical 5 | main 7: Sum until zero"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

total=0
samples=iter(['5','-2','7','0'])
while True:
    raw=next(samples) if '--demo' in sys.argv else ask('Number; 0 stops',0)
    n=float(raw)
    if n==0: break
    if n<0: continue
    total+=n
print('Sum:',total)
