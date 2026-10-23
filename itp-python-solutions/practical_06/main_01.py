"""Practical 6 | main 1: List matrix creation"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix); print('First row:',matrix[0]); print('Row 2, column 3:',matrix[1][2])
