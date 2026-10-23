"""Practical 10 | main 12: Paragraph analysis"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

import re
from collections import Counter
text=ask('Paragraph','Python is fun. Python makes coding fun!')
words=re.findall(r"\b\w+(?:'\w+)*\b",text.lower()); counts=Counter(words)
print('Word count:',len(words),'Character count including spaces:',len(text))
if counts:
    top=max(counts.values()); print('Most frequent words:',[w for w,c in counts.items() if c==top],'Count:',top)
else: print('No words to analyze')
