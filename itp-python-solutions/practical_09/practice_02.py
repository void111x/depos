"""Practical 9 | practice 2: BMI function"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def calculate_bmi(weight,height):
    if weight<=0 or height<=0: raise ValueError('Positive weight and height required')
    bmi=weight/height**2
    category='Underweight' if bmi<18.5 else 'Normal' if bmi<25 else 'Overweight' if bmi<30 else 'Obese'
    return bmi,category
bmi,category=calculate_bmi(72,1.75); print(f'{bmi:.2f}',category)
