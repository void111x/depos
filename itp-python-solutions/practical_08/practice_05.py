"""Practical 8 | practice 5: Token frequency"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text='python makes coding easy and python makes debugging easier'; counts={}
for word in text.split(): counts[word]=counts.get(word,0)+1
print(counts)
