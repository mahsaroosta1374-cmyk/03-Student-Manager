from my_package.student_manager import Student, StudentManager

manager = StudentManager()
manager.load_students()

while True:
    print("\n ========== Student Manager ==========")
    print("1. Add New Student")
    print("2. Remove Student")
    print("3. Show all students")
    print("4. Search")
    print("5. Edit")
    print("6. Number of Students")
    print("7. Exit")
    
    choice = input("Please Enter Your Choice: ")
    
    if choice == "1":
        name = input("Please Enter Name:")
        student_ID = input("Plaese Enter Student_ID: ")
        major = input("Please Enter Major: ")
        student = Student(name, student_ID, major)
        manager.add_student(student)
        
    elif choice == "2":
        student_ID = input("Please Enter Student_ID to Remove: ")
        manager.remove_student(student_ID)
        
    elif choice == "3":
        manager.show_students()
        
    elif choice == "4":
        student_ID = input("Please Enter Student-ID: ")
        student = manager.search_student(student_ID)
        if student == None:
            print("The Student was not Found!")
        else:
            print(student)
    
    elif choice == "5":
            student_ID = input("Please Enter Student_ID: ")
            student = manager.search_student(student_ID)
            if student == None:
                print("The student was not Found!")
            else:
                print(student)
                new_name = input("Please Enter New Name: ")
                new_major = input("Please Enter New Major: ")
                manager.edit_student(student_ID, new_name, new_major)
                print("The Information was Seccessfully Saved!")
        
    elif choice == "6":
        manager.statistics()
        
    elif choice == "7":
        print("Goodbye!")
        break
    
    else:
        print("Invalid Choice! Please Try Again.")

        