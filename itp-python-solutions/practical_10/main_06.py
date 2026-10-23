"""Practical 10 | main 6: Find versus index"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text='Python makes coding easy'
print(text.find('coding'),text.index('coding'))
print('Missing find:',text.find('Java'))
try: print(text.index('Java'))
except ValueError: print('index raises ValueError when absent; find returns -1.')
