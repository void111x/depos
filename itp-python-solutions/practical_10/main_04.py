"""Practical 10 | main 4: String immutability"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text='python'
try: text[0]='P'
except TypeError: print('Strings do not support item assignment.')
text='P'+text[1:]; print(text)
