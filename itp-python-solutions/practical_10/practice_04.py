"""Practical 10 | practice 4: Password checks"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

password='PySecure2026!'
# Assumption: minimum length 8; special means nonalphanumeric, nonwhitespace.
checks={'uppercase':any(c.isupper() for c in password),'lowercase':any(c.islower() for c in password),'digit':any(c.isdigit() for c in password),'special':any(not c.isalnum() and not c.isspace() for c in password),'minimum_length':len(password)>=8}
print(checks); print('Valid:',all(checks.values()))
