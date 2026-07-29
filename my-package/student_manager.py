import csv

class Student():
    def __init__(self, name, student_ID, major):
        self.name = name
        self.student_ID = student_ID
        self.major = major
        
    def __str__(self):
        return f"name: {self.name}, student_ID: {self.student_ID}, major: {self.major}"
        

class StudentManager():
    def __init__(self):
        self.students = []
        
    def add_student(self, student):
        for item in self.students:
            if item.student_ID == student.student_ID:
                print("This ID Alraedy Exists.")
                return
        self.students.append(student)
        self.save_student()
        
    def remove_student(self, student_ID):
        for item in self.students:
            if item.student_ID == student_ID:
                self.students.remove(item)
                self.save_student()
                return
        print("Student Not Found")
        
    def show_students(self):
        print("This is the list of Students:")
        for items in self.students:
            print(items)
        
    def search_student(self, student_ID):
        for item in self.students:
            if item.student_ID == student_ID:
                print("This is the Student Information: ")
                return item
        return None
            
    def edit_student(self, student_ID, new_name, new_major):
        for item in self.students:
            if item.student_ID == student_ID:
                item.name = new_name
                item.major = new_major
                self.save_student()
                return
            
    def statistics(self):
        print(f"Total Students: {len(self.students)}")
        
    def save_student(self):
        fieldnames = ("name", "student_ID", "major")
        with open("studentmanager.csv", mode = "w", newline = "") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in self.students:
                student_dict = {"name": item.name, "student_ID": item.student_ID, "major": item.major}
                writer.writerow(student_dict)
    
    def load_students(self):
        self.students = []
        try:
            with open("studentmanager.csv", mode = "r", newline = "") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(row["name"], row["student_ID"], row["major"])
                    self.students.append(student)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    print("you should use me as a package")
    
