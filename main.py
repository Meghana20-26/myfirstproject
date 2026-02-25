students = []
def add_student():
    name = input("Enter Name:")
    roll = input("Enter Roll Number:")
    for s in students:
        if s["roll"]==roll:
            print("Roll Number already exists.")
            return
        try:
            marks = float(input("Enter Marks:"))
        except:
            print("Invalid marks.")
            return
        if marks >=75:
            grade = "A"
        elif marks >=60:
            grade = "B"
        elif marks >=40:
            grade = "C"
        else:
            grade = "Fail"

            student = {
                "name":name,
                "roll":roll,
                "marks":marks,
                "grade":grade
            }
            students.append(student)
            print("student added sucessfully.\n")

            def search_student():
                roll = input("Enter Roll Number to search:")

                for s in students:
                    if s["roll"] == roll:
                        print("Student Found:")
                        print(s)
                        return
                    print("Student not Found.\n")

                    def calculate_average():
                        if len(students) == 0:
                            print("No of Records Available.\n")
                            return
                        top = students[0]
                        for s in students:
                            if s["marks"] > top["marks"]:
                                top = s
                            print("Topper is :",top["marks"],"with",top["marks"],"marks")
                            def view_students():
                                def Display_Topper():
                                    while True:
                                        print("\n1. Add Student")
                                        print("2. view Student")
                                        print("3. search Student")
                                        print("4. Average Marks")
                                        print("5. Display Topper")
                                        print("6. Exit")
                                        choice = input("Enter choice:")
                                        if choice == "1":
                                            add_student()
                                        elif choice == "2":
                                            view_students()
                                        elif choice == "3":
                                            search_student()
                                        elif choice == "4":
                                            calculate_average()
                                        elif choice == "5":
                                            display_Topper()
                                        elif choice == "6":
                                            print("Program Ended.")
                                            break
                                        else:
                                            print("Invalid choice.")



                        

            