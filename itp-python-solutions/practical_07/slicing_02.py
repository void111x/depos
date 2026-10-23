"""Practical 7 | slicing 2: Rows and columns"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print('Second row:',matrix[1])
print('Third column:')
for row in matrix: print(row[2])
print('Each row is a separate list; extract the column element from each row.')
