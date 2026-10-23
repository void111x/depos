"""Practical 10 | practice 3: Flight log splitting"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

log='ALT:250|SPD:45|BAT:78'; values={}
for part in log.split('|'):
    key,value=part.split(':',1); values[key]=int(value)
print('Altitude:',values['ALT'],'Speed:',values['SPD'],'Battery:',values['BAT'])
