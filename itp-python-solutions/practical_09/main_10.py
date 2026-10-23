"""Practical 9 | main 10: Local and global scope"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

value=10
def local_change():
    value=20
    print('Local:',value)
def global_change():
    global value
    value=30
local_change(); print('Global after local change:',value)
global_change(); print('Global after global change:',value)
