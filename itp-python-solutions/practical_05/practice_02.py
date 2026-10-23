"""Practical 5 | practice 2: Skip duplicate RFID"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

entries=[f'CARD{i%45+1:03d}' for i in range(60)]  # 60 example scans.
seen=set()
for card in entries:
    if card in seen: continue
    seen.add(card)
    print('Recorded',card)
print('Unique attendance:',len(seen))
