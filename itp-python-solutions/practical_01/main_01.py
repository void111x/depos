"""Practical 1 | main 1: Variables and naming rules"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

name, age, marks, city = "Ishaan", 18, 85.5, "Mumbai"
print(name, age, marks, city)
for source in ['1name = "Python"', 'class = 1', 'my-name = 1']:
    try:
        compile(source, '<example>', 'exec')
    except SyntaxError as error:
        print(source, '-> SyntaxError:', error.msg)
name1, class_name, my_name = 'Python', 1, 'Ishaan'
print('Names cannot start with digits, use keywords, or contain hyphens.')
