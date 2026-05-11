# Rikki Kratochvil
# Assignment 8.2
# CSD-325 Module 8

import json


def print_students(student_list):
    """Print each student in the required format."""
    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


# Load the JSON file into a Python list
with open(r"C:\Users\krato\Documents\BU\Advanced Python\student.json", "r") as file:
    students = json.load(file)

print("Original Student List:")
print_students(students)

# Add your information to the student list
new_student = {
    "F_Name": "Rikki",
    "L_Name": "Kratochvil",
    "Student_ID": 12471,
    "Email": "rkratochvil@gmail.com"
}

students.append(new_student)

print("\nUpdated Student List:")
print_students(students)

# Save the updated list back to the JSON file
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("\nThe student.json file was updated.")