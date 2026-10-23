"""Practical 4 | main 3: Loop accumulation"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

n=int(ask('How many numbers',3))
if n<=0: raise ValueError('Count must be positive')
total=0
for i in range(n): total+=float(ask(f'Number {i+1}',i+1))
print('Sum:',total,'Average:',total/n)
