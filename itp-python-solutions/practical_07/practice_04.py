"""Practical 7 | practice 4: Deduplicate songs"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

songs=['Shape of You','Believer','Perfect','Believer','Faded','Perfect','Senorita','Levitating','Faded','Perfect','Blinding Lights','Senorita','Peaches','Believer','Perfect']
unique=[]
for song in songs:
    if song not in unique: unique.append(song)
print(unique)
