"""Practical 7 | practice 6: Quiz score slices"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

scores=[78,85,91,88,76,95,89,84]
for name,data in [('Midterm',scores[:4]),('Final',scores[-4:]),('Overall',scores)]:
    print(name,data,'Highest:',max(data),'Average:',sum(data)/len(data))
