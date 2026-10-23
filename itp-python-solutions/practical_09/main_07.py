"""Practical 9 | main 7: Recursive factorial and trace"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def factorial(n):
    if n<0: raise ValueError('n must be nonnegative')
    print('Call factorial:',n)
    if n<=1: return 1
    result=n*factorial(n-1)
    print('Return factorial:',n,result)
    return result
n=int(ask('Small nonnegative integer',5))
recursive=factorial(n); iterative=1
for i in range(1,n+1): iterative*=i
print('Recursive:',recursive,'Iterative:',iterative)
print('Both O(n) time; recursion uses O(n) call-stack space, loop O(1) auxiliary space.')
