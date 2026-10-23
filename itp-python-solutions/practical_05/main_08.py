"""Practical 5 | main 8: Three password attempts"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

PASSWORD='Python123'  # Classroom demonstration only.
for attempt in range(1,4):
    entered=ask(f'Password attempt {attempt}', 'wrong' if attempt<3 else PASSWORD)
    if entered==PASSWORD:
        print('Access granted')
        break
else: print('Access denied after 3 attempts')
