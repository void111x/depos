"""Practical 5 | practice 7: Future plagiarism check"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def ai_plagiarism_check(answer):
    pass  # Reserved for future implementation.
print(ai_plagiarism_check('Sample answer'))
print('A function with no return currently returns None.')
