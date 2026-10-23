"""Practical 7 | practice 9: Stock price positions"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

prices=[210,215,208,220,225,230,218,240,235,245]
ranked=sorted(enumerate(prices,1),key=lambda pair:pair[1],reverse=True)
print('Top three (position, price):',ranked[:3])
print('Lowest slots:',[i+1 for i,p in enumerate(prices) if p==min(prices)],'Price:',min(prices))
