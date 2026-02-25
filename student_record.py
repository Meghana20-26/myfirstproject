students = []

def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print("Roll number already exists.\n")
            return

    try:
        marks = float(input("Enter Marks: "))
    except:
        print("Invalid marks.\n")
        return

    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students.append({
        "name": name,
        "roll": roll,
        "marks": marks,
        "grade": grade
    })

    print("Student added successfully.\n")


def view_students():
    if not students:
        print("No records available.\n")
        return

    for s in students:
        print("Name:", s["name"])
        print("Roll:", s["roll"])
        print("Marks:", s["marks"])
        print("Grade:", s["grade"])
        print()


def search_student():
    roll = input("Enter Roll Number to search: ")

    for s in students:
        if s["roll"] == roll:
            print("Student Found:")
            print("Name:", s["name"])
            print("Roll:", s["roll"])
            print("Marks:", s["marks"])
            print("Grade:", s["grade"])
            print()
            return

    print("Student not found.\n")


def calculate_average():
    if not students:
        print("No records available.\n")
        return

    total = 0
    for s in students:
        total += s["marks"]

    average = total / len(students)
    print("Average Marks:", round(average, 2), "\n")


def display_topper():
    if not students:
        print("No records available.\n")
        return

    topper = students[0]

    for s in students:
        if s["marks"] > topper["marks"]:
            topper = s

    print("Topper Details")
    print("Name:", topper["name"])
    print("Roll:", topper["roll"])
    print("Marks:", topper["marks"])
    print("Grade:", topper["grade"])
    print()


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Average Marks")
    print("5. Display Topper")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        calculate_average()
    elif choice == "5":
        display_topper()
    elif choice == "6":
        print("Program Ended.")
        break
    else:
        print("Invalid choice.\n")

