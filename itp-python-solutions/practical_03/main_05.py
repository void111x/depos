"""Practical 3 | main 5: Largest including ties"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a,b,c=map(float,ask('Three numbers','7 7 3').split())
if a>=b and a>=c: largest=a
elif b>=a and b>=c: largest=b
else: largest=c
print('Largest:',largest,'Positions:',[i+1 for i,x in enumerate((a,b,c)) if x==largest])
