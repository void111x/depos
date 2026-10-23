"""Practical 9 | main 12: Student result functions"""

import sys

def ask(prompt, default):
    """Use sample values with --demo; otherwise accept keyboard input."""
    if "--demo" in sys.argv:
        print(f"{prompt} [{default}]")
        return str(default)
    value = input(f"{prompt} [{default}]: ")
    return value if value.strip() else str(default)

def input_marks():
    marks=list(map(float,ask('Marks out of 100','90 80 70').split()))
    if not marks or any(not 0<=m<=100 for m in marks): raise ValueError('Enter marks between 0 and 100')
    return marks
def calculate(marks): return sum(marks),sum(marks)/len(marks)
def grade(percentage):
    return 'A' if percentage>=90 else 'B' if percentage>=75 else 'C' if percentage>=50 else 'Fail'
def main():
    marks=input_marks(); total,percentage=calculate(marks)
    print(f'Total: {total}/{100*len(marks)}; percentage: {percentage:.2f}; grade: {grade(percentage)}')
main()
