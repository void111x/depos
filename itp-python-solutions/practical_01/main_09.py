"""Practical 1 | main 9: Type-based calculator"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import ast
# Numeric literals add; plain text joins. Other literal types are rejected.
def parse(text):
    try:
        return ast.literal_eval(text)
    except (ValueError, SyntaxError):
        return text
x, y = parse(ask('First value', 12)), parse(ask('Second value', 3.5))
print('Types:', type(x).__name__, type(y).__name__)
if type(x) in (int, float) and type(y) in (int, float):
    print(x + y)
elif isinstance(x, str) and isinstance(y, str):
    print(x + y)
else:
    print('Invalid combination: enter two numbers or two strings.')
