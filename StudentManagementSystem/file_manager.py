from student import Student
class FileManager:
    def __init__(self):
        self.students = []
    def save_students(self, filename, students):
        with open(filename, "w") as file:
            for s in students:
                file.write(f"{s.id}, {s.name}, {s.age}, {s.grade}, {s.email}\n")
    def load_students(self, filename):
        try:
            self.students = []
            with open(filename, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    id, name, age, grade, email = line.split(', ')
                    student = Student(id, name, int(age), grade, email)
                    self.students.append(student)
        except FileNotFoundError:
            print("No student records found.")
        return self.students
    def append_student(self, filename, student):
        with open(filename, "a") as file:
            file.write(f"{student.id}, {student.name}, {student.age}, {student.grade}, {student.email}\n")
    def delete_file_Data(self, filename):
        with open(filename, "w") as file:
            pass
    def delete_File(self, filename):
        import os
        if os.path.exists(filename):
            os.remove(filename)
            print("File deleted successfully...")
        else:
            print(f"{filename} doesn't exist\n")