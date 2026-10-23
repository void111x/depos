"""Practical 10 | main 7: Count occurrences"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text='banana banana'; print('a count:',text.count('a'),'banana count:',text.count('banana'))
print('count counts non-overlapping, case-sensitive substrings.')
