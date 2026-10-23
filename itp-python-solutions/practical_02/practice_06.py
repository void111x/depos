"""Practical 2 | practice 6: Topper positions"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

marks=list(map(float,ask('Five marks','78 91 85 67 95').split()))
if len(marks)!=5: raise ValueError('Enter exactly five marks')
top=max(marks)
print('Top marks:',top,'Student positions:',[i+1 for i,m in enumerate(marks) if m==top])
