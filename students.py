'''📘 Student Registration System (English Version)
Create a program that allows registering students and their grades.

Requirements
The program must have a list called students.
Each student must be represented by a dictionary containing:

name

age

grade

Create functions to:

add a student

list all students

show approved students

A student is considered approved if their grade is greater than or equal to 10 (scale 0–20).

The program must use conditions (if statements) to check approval.'''


import json
from pathlib import Path
import os

ROOT_FOLDER = Path(__file__).parent
JSON_FILE = ROOT_FOLDER / 'students.json'
#-----------------------------------------------------------
def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#-----------------------------------------------------------
def save_students(students):
    with open(JSON_FILE, 'w', encoding="utf-8" ) as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
#-----------------------------------------------------------
def load_students():
    if JSON_FILE.exists():
        with open(JSON_FILE,'r', encoding='utf-8') as f:
            return json.load(f)
    return []
#----------------------------------------------------------

def add_students(students, name, age, exam_grade):
    
    data = {'name': name, 'age': age, 'exam_grade': exam_grade}
    students.append(data)
#----------------------------------------------------------
def list_students(students):
    screen_clear()
    sort_students = sorted(students, key=lambda s: s['name'])
    for student in sort_students:
        print(
            f"\nName: {student['name']}"
            f"\nAge: {student['age']}"
            f"\nExam Grade: {student['exam_grade']:.2f}"
        )
    input("\nPress enter to back to the Menu...")
#----------------------------------------------------------
def approved_student(students):
    screen_clear()
    sort_students = sorted(students, key=lambda s: s['name'])
    approved_students = []

    for student in sort_students:
        if student['exam_grade'] >= 10:
            approved_students.append(student)
        
    if not approved_students:
        print('\nNo approved students')

    else:
        print("\n------------------------")
        print("  Approved students 🎉")
        print("------------------------")

        for student in approved_students:
            print(
                f"\nName: {student['name']}"
                f"\nAge: {student['age']}"
                f"\nExam Grade: {student['exam_grade']:.2f}"
            )
    input("\nPress enter to back to the Menu...")
#----------------------------------------------------------

# 💻 MAIN PROGRAM 💻
students = load_students()

while True:
    screen_clear()
    print("[1] Add students")
    print("[2] list students")
    print("[3] list of approved students ")
    print("[4] Exit ")
    
    try:
        opt = int(input("\nenter an option: "))
        if opt < 1 or opt > 4:
            print("Option invalid.")
            input("\nPress any key to continue...")
            continue
    except ValueError:
        print("\nOption invalid.")
        continue

    match opt:
        case 1:
            while True:
                name = input("Enter the name's student: ").strip()
                if name.isdigit():
                    print('não pode ter números.')
                    continue
                else:
                    break
            while True:
                try:
                    age = int(input("Enter the age's student: "))
                    break
                except ValueError:
                    print('age invalid')
                    continue

            while True:
                try:
                    exam_grade = float(input("Enter the exame grade's student: "))
                    if exam_grade < 0 or exam_grade > 20:
                        print("It cannot be greater than 20 or less than 0")
                    else:
                        break
                except ValueError:
                    print("Exam grade invalid.")
                    continue
            add_students(students, name, age, exam_grade)
            save_students(students)

        case 2:
            list_students(students)

        case 3:
            approved_student(students)
        
        case 4:
            break

print(students)