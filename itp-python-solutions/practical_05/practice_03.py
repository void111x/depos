"""Practical 5 | practice 3: Emergency triage"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

patients=[('P1','routine'),('P2','urgent'),('P3','critical'),('P4','routine')]
for patient,status in patients:
    if status=='critical':
        print('Emergency detected:',patient,'Stop routine queue.')
        break
    print('Processing',patient)
