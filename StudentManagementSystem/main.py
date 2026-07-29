from student import Student
from student_manager import StudentManager
from file_manager import FileManager
from validator import Validator
from report_manager import ReportManager

def main():
    manager = StudentManager()
    file_manager = FileManager()
    validator = Validator()
    report_manager = ReportManager(manager.students)

    filename = "students.txt"
    manager.students = file_manager.load_students(filename)
    report_manager.students = manager.students

    while True:
            print("\n========== Student Management System ==========")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Display All Students")
            print("6. Sort by Name")
            print("7. Sort by Grade")
            print("8. Student Statistics")
            print("9. Save Students")
            print("10. Load Students")
            print("11. Exit")
            
            choice = input("Enter your choice : ")
            
            # _____________ ADD _____________
            if choice=="1":
                id = input("Enter Student ID (8 digit): ")
                if not validator.validate_id(id):
                    print("Invalid ID")
                    continue
                if manager.searchStudent(id):
                    print("ID already exists")
                    continue
                name = input("Enter name : ")
                if not validator.validate_name(name):
                    print("Invalid name...")
                    continue
                try:
                    age = int(input("Enter age : "))
                except ValueError:
                    print("Invalid Age")
                    continue
                if not validator.validate_age(age):
                    print("Invalid Age")
                    continue
                grade = input("Enter grade: ")
                if not validator.validate_grade(grade.upper()):
                    print("Invalid Grade")
                    continue
                email = input("Enter Email: ")
                if not validator.validate_email(email):
                    print("Invalid Email")
                    continue
                student = Student(id, name, age, grade, email)
                manager.addStudent(student)
                print("Student added successfully")
                
            # _____________ Delete _____________
            elif choice=="2":
                id = input("Enter ID of student to delete : ")
                if manager.remove(id):
                    print(f"Student with {id} has been deleted.")
                else:
                    print("Student Not Found")
            # _____________ Search _____________
            elif choice=="3":
                id = input("Enter id to search student: ")
                student = manager.searchStudent(id)
                if student:
                    student.display()
                else:
                    print("No student found")
            # _____________ Update _____________
            elif choice=="4":
                id = input("Enter Student ID to update record: ")
                manager.updateStudent(id)
            # _____________ Display All students _____________
            elif choice=="5":
                manager.display_AllStudents()
            # _____________ Sort by Name _____________
            elif choice=="6":
                manager.sort_by_Name()
            # _____________ Sort by Grade _____________
            elif choice=="7":
                manager.sort_by_Grade()
            # _____________ Student Statistics _____________
            elif choice=="8":
                report_manager.students_statistics()
            # _____________ Save students _____________
            elif choice=="9":
                file_manager.save_students(filename, manager.students)
            # _____________ Load students _____________
            elif choice=="10":
                manager.students = file_manager.load_students(filename)
                report_manager.students = manager.students
            # _____________ Display All students _____________
            elif choice=="11":
                save = input("Save before exiting? (y/n): ")
                if save.lower() =="y":
                    file_manager.save_students(filename, manager.students)
                print("Goodbye!")
                break
            else:
                print("Invalid Choice")
if __name__ == "__main__":
    main()