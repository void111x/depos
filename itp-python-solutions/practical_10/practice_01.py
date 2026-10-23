"""Practical 10 | practice 1: Chatbot text cleanup"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

text='   Python   makes   NLP   powerful   '
clean=' '.join(text.split()).lower(); words=clean.split()
print(clean); print(words); print('_'.join(words))
