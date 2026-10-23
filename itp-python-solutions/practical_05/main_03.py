"""Practical 5 | main 3: Break versus continue"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

print('Break:')
for n in range(1,11):
    if n==5: break
    print(n,end=' ')
print('\nContinue:')
for n in range(1,11):
    if n==5: continue
    print(n,end=' ')
print('\nBreak ends the loop; continue skips only this iteration.')
