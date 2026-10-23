"""Practical 10 | main 11: Palindrome slicing"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text=ask('Text','Madam')
# Assumption: ignore case, whitespace, and punctuation.
normalized=''.join(c.lower() for c in text if c.isalnum())
print('Reverse:',normalized[::-1]); print('Palindrome:',bool(normalized) and normalized==normalized[::-1])
