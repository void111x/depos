"""Practical 2 | main 5: Salary breakdown"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

basic = float(ask('Basic salary', 30000))
if basic < 0: raise ValueError('Salary must be nonnegative')
hra,da = basic*.2,basic*.1
print(f'Basic: {basic:.2f}\nHRA: {hra:.2f}\nDA: {da:.2f}\nNet: {basic+hra+da:.2f}')
# No deductions specified; worksheet net equals basic plus allowances.
