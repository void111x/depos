"""Practical 2 | main 7: Unit conversions"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

km,c,rupees = [float(ask(n,v)) for n,v in [('Kilometres',2.5),('Celsius',37),('Rupees',830)]]
INR_PER_USD = 83  # Assumed fixed classroom rate, not a live exchange rate.
print(f'{km*1000:.2f} m; {c*9/5+32:.2f} F; USD {rupees/INR_PER_USD:.2f}')
