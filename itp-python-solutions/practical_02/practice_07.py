"""Practical 2 | practice 7: Simple-interest monthly instalment"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

principal,months,annual_rate=500000,24,12
interest=principal*annual_rate/100*(months/12)
print(f'Interest: {interest:.2f}; total: {principal+interest:.2f}; monthly: {(principal+interest)/months:.2f}')
print('Worksheet uses simple interest; this is not reducing-balance EMI.')
