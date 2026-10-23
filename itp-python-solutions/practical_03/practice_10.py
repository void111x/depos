"""Practical 3 | practice 10: Service bonus"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

years=float(ask('Years of service',10)); salary=float(ask('Salary',30000))
if min(years,salary)<0: raise ValueError('Values must be nonnegative')
if years>=10: rate=.2
elif years>=5: rate=.1
else: rate=0
print(f'Bonus rate: {rate:.0%}; bonus: {salary*rate:.2f}')
