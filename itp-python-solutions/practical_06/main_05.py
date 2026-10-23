"""Practical 6 | main 5: Transpose lists"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

rows=int(ask('Rows',2)); cols=int(ask('Columns',3))
if min(rows,cols)<=0: raise ValueError('Dimensions must be positive')
matrix=[]
for r in range(rows):
    row=list(map(float,ask(f'Row {r+1}',' '.join(str(r*cols+c+1) for c in range(cols))).split()))
    if len(row)!=cols: raise ValueError('Wrong column count')
    matrix.append(row)
transpose=[[matrix[r][c] for r in range(rows)] for c in range(cols)]
print('Original:',matrix,'Transpose:',transpose)
