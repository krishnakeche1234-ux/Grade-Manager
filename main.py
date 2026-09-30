students = {}


def add_student():
    name = input("Enter the student's name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks out of 100: "))
    except ValueError:
        print("Please enter a number for the marks.")
        return

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        return

    students[name] = marks
    print(f"Marks saved for {name}.")


def view_students():
    if not students:
        print("No students have been added yet.")
        return

    print("\n--- Student Grades ---")
    for name, marks in students.items():
        print(f"{name}: {marks:g}/100")


def find_student():
    name = input("Enter the student's name to search: ").strip()

    if name in students:
        marks = students[name]
        print(f"{name} scored {marks:g}/100.")
    else:
        print("Student not found.")


while True:
    print("\n=== Student Grade Manager ===")
    print("1. Add or update student marks")
    print("2. View all students")
    print("3. Find a student")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        find_student()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose a number from 1 to 4.")1
        