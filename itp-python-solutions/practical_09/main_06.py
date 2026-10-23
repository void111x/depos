"""Practical 9 | main 6: List processing function"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def summarize(numbers):
    if not numbers: return 0,None
    total=0; largest=numbers[0]
    for n in numbers:
        total+=n
        if n>largest: largest=n
    return total,largest
for values in ([1,4,2],[10,-2,8],[]): print(values,summarize(values))
