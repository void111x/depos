"""Practical 1 | main 6: Implicit and explicit conversion"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

print(10 + 2.5, type(10 + 2.5))
try:
    print(10 + '5')
except TypeError:
    print('int + str raises TypeError: no automatic string-to-number conversion.')
print(10 + int('5'))
print('int + float promotes the numeric result to float.')
