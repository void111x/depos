"""Practical 5 | main 4: Linear search"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

numbers=list(map(int,ask('Numbers','4 8 3 8').split())); target=int(ask('Target',8))
for index,value in enumerate(numbers):
    if value==target:
        print('Index:',index,'Position:',index+1)
        break
else: print('Not found')
