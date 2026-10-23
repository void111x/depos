"""Practical 9 | practice 5: Text sanitizing function"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def sanitize(text):
    clean=' '.join(text.lower().split())
    return clean,len(clean.split())
print(sanitize('Python   Makes   AI   Easy'))
