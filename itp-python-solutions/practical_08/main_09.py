"""Practical 8 | main 9: Nested students"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

students={'S1':{'name':'Asha','marks':92},'S2':{'name':'Ravi','marks':85}}
print(students['S1']['name']); students['S2']['marks']=90; print(students)
