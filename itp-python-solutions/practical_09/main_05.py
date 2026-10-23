"""Practical 9 | main 5: Built-in functions"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

numbers=[3,1,4,2]; text='Python'
print(len(numbers),sum(numbers),max(numbers),min(numbers))
print('String:',len(text),max(text),min(text))
count=total=0; largest=smallest=numbers[0]
for n in numbers:
    count+=1; total+=n
    if n>largest: largest=n
    if n<smallest: smallest=n
print('Manual:',count,total,largest,smallest)
try: sum(text)
except TypeError: print('sum is numeric; strings are joined using join, not sum.')
