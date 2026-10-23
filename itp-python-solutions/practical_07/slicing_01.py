"""Practical 7 | slicing 1: Matrix element indexing"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][0],matrix[-1][-1],matrix[1][1])
