"""Practical 3 | practice 2: Loan conditions"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

salary=float(ask('Salary',30000)); credit=int(ask('Credit score',701))
print('Approved' if salary>=30000 and credit>700 else 'Rejected')
