"""Practical 10 | practice 2: Student ID masking"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

student_id='STU2026CS1098'; print(student_id[:4]); print(student_id[-4:]); print(student_id[:4]+'****'+student_id[-4:])
