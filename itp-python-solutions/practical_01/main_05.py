"""Practical 1 | main 5: Explicit casting"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

age_text, marks_text = ask('Age', 18), ask('Marks', 85.5)
age, marks = int(age_text), float(marks_text)
print('Age next year:', age + 1, 'Marks plus 5:', marks + 5)
try:
    print(age_text + 1)
except TypeError:
    print('TypeError: input is a string; convert before numeric addition.')
print('Without conversion, + joins strings:', age_text + '1')
