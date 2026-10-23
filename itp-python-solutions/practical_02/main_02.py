"""Practical 2 | main 2: Numeric input"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

a_text, b_text = ask('First number', 25), ask('Second number', 4)
print('Strings concatenate:', a_text + b_text)
a, b = float(a_text), float(b_text)
print('Sum:', a+b, 'Difference:', a-b, 'Product:', a*b)
print('Quotient:', a/b if b else 'Cannot divide by zero')
