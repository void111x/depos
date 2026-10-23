"""Practical 5 | practice 10: Repeated suspicious IP"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

# Documentation-only example addresses; suspicious set supplied as sample policy.
suspicious={'192.0.2.9'}
attempts=['192.0.2.9','198.51.100.2','192.0.2.9','203.0.113.7','192.0.2.9','198.51.100.2']
counts={}
for ip in attempts:
    print('Checking',ip)
    if ip not in suspicious: continue
    counts[ip]=counts.get(ip,0)+1
    if counts[ip]==3:
        print('Halt: suspicious IP seen three times:',ip)
        break
