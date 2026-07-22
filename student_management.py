import json
import os

FILE = "students.json"

def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE, "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        course = input("Course: ")

        students.append({
            "ID": sid,
            "Name": name,
            "Age": age,
            "Course": course
        })

        save_students(students)
        print("Student Added Successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for s in students:
                print(s)

    elif choice == "3":
        sid = input("Enter Student ID: ")
        found = False
        for s in students:
            if s["ID"] == sid:
                print(s)
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        sid = input("Enter Student ID: ")
        found = False
        for s in students:
            if s["ID"] == sid:
                s["Name"] = input("New Name: ")
                s["Age"] = input("New Age: ")
                s["Course"] = input("New Course: ")
                save_students(students)
                print("Student Updated Successfully!")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "5":
        sid = input("Enter Student ID: ")
        students = [s for s in students if s["ID"] != sid]
        save_students(students)
        print("Student Deleted Successfully!")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid Choice! Please try again.")