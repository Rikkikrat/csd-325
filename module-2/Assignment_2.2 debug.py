# Rikki Kratochvil
# 03/25/2026
# Assignment 2.2
# Purpose: Calculate letter grade

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    print("Welcome to the Grade Calculator")
    student_name = input("Enter the student's name: ")
    score = float(input("Enter the student's numeric score: "))

    letter_grade = get_letter_grade(score)

    print("\n--- Grade Summary ---")
    print("Student Name:", student_name)
    print("Numeric Score:", score)
    print("Letter Grade:", letter_grade)

main()