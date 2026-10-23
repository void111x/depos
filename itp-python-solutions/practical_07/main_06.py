"""Practical 7 | main 6: Remove and pop"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

items=['a','b','c']; items.remove('b'); print(items)
print('Popped:',items.pop()); print(items)
try: items.remove('missing')
except ValueError: print('remove raises ValueError when the value is absent.')
items.pop()
try: items.pop()
except IndexError: print('pop raises IndexError on an empty list.')
