"""Practical 9 | main 8: Recursive Fibonacci"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n<0: raise ValueError('n must be nonnegative')
    if n<2: return n
    return fibonacci(n-1)+fibonacci(n-2)
n=int(ask('Number of terms',8))
if n<0: raise ValueError('Count must be nonnegative')
print('Recursive:',[fibonacci(i) for i in range(n)])
a,b=0,1; values=[]
for _ in range(n):
    values.append(a); a,b=b,a+b
print('Iterative:',values)
print('Naive recursion repeats work exponentially. Memoization gives O(n) work/storage; iteration avoids recursion overhead.')
