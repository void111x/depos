"""Practical 4 | practice 9: Predict Fibonacci"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a,b=0,1
for i in range(5):
    print(a,end=' ')
    a,b=b,a+b
print()
