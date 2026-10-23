"""Practical 4 | main 10: Nested loop patterns"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

n=int(ask('Rows',4))
for reverse in (False,True):
    print('Reverse stars' if reverse else 'Stars')
    for row in (range(n,0,-1) if reverse else range(1,n+1)):
        for col in range(row): print('*',end='')
        print()
for reverse in (False,True):
    print('Reverse numbers' if reverse else 'Numbers')
    for row in (range(n,0,-1) if reverse else range(1,n+1)):
        for col in range(1,row+1): print(col,end=' ')
        print()
