"""Practical 8 | main 2: Key access"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

student={'Name':'Ishaan','Age':18,'Marks':85}
print(student['Name'],student['Age'],student['Marks'])
try: print(student['City'])
except KeyError: print('Direct access to an absent key raises KeyError.')
