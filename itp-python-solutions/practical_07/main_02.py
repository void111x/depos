"""Practical 7 | main 2: Positive and negative indexing"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

for data in ([10,20,30,40,50],('a','b','c','d','e')):
    print('First:',data[0],data[-len(data)])
    print('Last:',data[len(data)-1],data[-1])
    print('Middle:',data[len(data)//2],data[-3])
