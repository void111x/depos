"""Practical 7 | practice 1: Recent book returns"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

books=[1045,1098,1120,1087,1155,1178,1201,1199,1180,1166,1134,1102]
# Assume supplied history is newest first, so oldest is at the end.
books.insert(0,1215); print('Removed oldest:',books.pop()); print(books)
