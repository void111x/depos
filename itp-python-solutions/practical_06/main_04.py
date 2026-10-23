"""Practical 6 | main 4: Matrix addition using loops"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

rows=int(ask('Rows',2)); cols=int(ask('Columns',2))
if min(rows,cols)<=0: raise ValueError('Dimensions must be positive')
def read_matrix(name):
    result=[]
    for r in range(rows):
        row=list(map(float,ask(f'{name} row {r+1}',' '.join(str(r*cols+c+1) for c in range(cols))).split()))
        if len(row)!=cols: raise ValueError('Wrong column count')
        result.append(row)
    return result
a,b=read_matrix('A'),read_matrix('B')
result=[]
for r in range(rows):
    row=[]
    for c in range(cols): row.append(a[r][c]+b[r][c])
    result.append(row)
print(result)
