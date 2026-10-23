"""Practical 6 | main 2: Matrix traversal"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print('Rows:')
for row in matrix:
    for value in row: print(value,end=' ')
    print()
print('Columns:')
for col in range(len(matrix[0])):
    for row in range(len(matrix)): print(matrix[row][col],end=' ')
    print()
