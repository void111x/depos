"""Practical 5 | practice 5: PIN retry limit"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

PIN='482931'; failures=0
# Resolve conflicting wording: retries are capped at five failures.
while True:
    entered=ask('Six-digit PIN', 'wrong' if failures<2 else PIN)
    if len(entered)==6 and entered.isdigit() and entered==PIN:
        print('Unlocked')
        break
    failures+=1
    print('Failed attempt',failures)
    if failures>=5:
        print('Locked after five failures')
        break
