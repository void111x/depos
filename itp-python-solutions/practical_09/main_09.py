"""Practical 9 | main 9: Function composition"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def read_number(): return float(ask('Number',5))
def process(number): return number**2
def display(result): print('Square:',result)
def main(): display(process(read_number()))
main()
