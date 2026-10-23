"""Practical 7 | practice 10: Room counts"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

from collections import Counter
rooms=('A101','A102','A103','B201','B202','B203','C301','C302','C303','A101','B201')
print('A101 count:',rooms.count('A101'),'C302 index:',rooms.index('C302'))
counts=Counter(rooms)
print('Repeated room IDs:',{room:count for room,count in counts.items() if count>1})
print('Floor/category counts:',dict(Counter(room[0] for room in rooms)))
