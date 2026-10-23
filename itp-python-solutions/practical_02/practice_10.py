"""Practical 2 | practice 10: BMI classroom calculation"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

weight,height=72,1.75
bmi=weight/height**2
category='Underweight' if bmi<18.5 else 'Normal' if bmi<25 else 'Overweight' if bmi<30 else 'Obese'
print(f'BMI: {bmi:.2f}; category: {category}')
# Assumed adult classroom thresholds; not an individual medical assessment.
