"""Practical 3 | main 10: Conditional menu"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

print('1. Even/odd  2. Largest of three  3. Grade')
choice=ask('Choice',1)
if choice=='1':
    n=int(ask('Integer',5)); print('Even' if n%2==0 else 'Odd')
elif choice=='2':
    a,b,c=map(float,ask('Three numbers','1 9 3').split()); print(max(a,b,c))
elif choice=='3':
    m=float(ask('Marks',85))
    if not 0<=m<=100: raise ValueError('Marks must be 0 to 100')
    print('A' if m>=90 else 'B' if m>=75 else 'C' if m>=50 else 'Fail')
else: print('Invalid choice')
