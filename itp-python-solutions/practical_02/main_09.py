"""Practical 2 | main 9: Student grades"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

marks = list(map(float,ask('Three marks out of 100','90 80 70').split()))
if len(marks)!=3 or any(not 0<=m<=100 for m in marks): raise ValueError('Enter three marks from 0 to 100')
total=sum(marks); percentage=total/3
# Assumed grade thresholds match Practical 3.
grade='A' if percentage>=90 else 'B' if percentage>=75 else 'C' if percentage>=50 else 'Fail'
print(f'Total: {total}/300; percentage: {percentage:.2f}%; grade: {grade}')
