"""Practical 8 | practice 3: Drone dictionary"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

sensor={'altitude':250,'speed':45,'battery':78,'gps':'ACTIVE'}
sensor['wind_speed']=12; sensor.pop('gps')
print('Keys:',list(sensor.keys()),'Values:',list(sensor.values()))
