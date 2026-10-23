"""Practical 8 | practice 2: Patient temperatures"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

patients={'P001':{'name':'Asha','temp':98.6},'P002':{'name':'Ravi','temp':101.2},'P003':{'name':'Neha','temp':99.1}}
high=max(item['temp'] for item in patients.values())
print('Highest:',[(key,value) for key,value in patients.items() if value['temp']==high])
patients['P003']['temp']=100.4; print(patients)
