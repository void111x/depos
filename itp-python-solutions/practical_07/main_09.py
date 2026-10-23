"""Practical 7 | main 9: Nested lists"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

matrix=[[1,2],[3,4]]; print(matrix[1][0]); matrix[1][0]=99; print(matrix)
