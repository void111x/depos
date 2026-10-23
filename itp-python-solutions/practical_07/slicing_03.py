"""Practical 7 | slicing 3: Negative matrix indices"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print('Last row:',matrix[-1],matrix[2])
print('Last column:',[row[-1] for row in matrix],[row[2] for row in matrix])
print('Bottom right:',matrix[-1][-1],matrix[2][2])
