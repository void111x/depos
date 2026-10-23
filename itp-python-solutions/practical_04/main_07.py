"""Practical 4 | main 7: Digit counts"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

n=abs(int(ask('Integer',12035)))
total=even=odd=0
if n==0: total=even=1
while n:
    digit=n%10; total+=1
    if digit%2==0: even+=1
    else: odd+=1
    n//=10
print('Total:',total,'Even:',even,'Odd:',odd)
