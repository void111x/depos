"""Practical 1 | main 4: Data type identification"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

integer = int(ask('Integer', 10))
decimal = float(ask('Float', 3.5))
text = ask('String', 'Python')
raw = ask('Boolean true/false', 'true').strip().lower()
if raw not in ('true', 'false'):
    raise ValueError('Enter true or false')
boolean = raw == 'true'
print(f'{"Value":<20}Type')
for value in (integer, decimal, text, boolean):
    print(f'{str(value):<20}{type(value).__name__}')
