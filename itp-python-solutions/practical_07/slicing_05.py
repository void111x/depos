"""Practical 7 | slicing 5: List submatrix"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
sub=[row[:2] for row in matrix[:2]]
print(sub)
print('Lists do not accept matrix[:2, :2]; slice each selected row separately.')
