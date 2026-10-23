"""Practical 8 | main 8: Character frequency"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text=ask('Text','hello world'); counts={}
for character in text: counts[character]=counts.get(character,0)+1
print(counts)  # Case-sensitive; includes spaces.
