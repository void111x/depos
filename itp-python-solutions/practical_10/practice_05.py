"""Practical 10 | practice 5: Symptom frequency"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

from collections import Counter
report='fever cough fever fatigue fever cold'; counts=Counter(report.split())
print('Fever:',counts['fever'],'Unique symptoms:',list(counts),'Unique count:',len(counts))
top=max(counts.values()); print('Most repeated:',[s for s,n in counts.items() if n==top])
