class StudentManager:
    def __init__(self):
        self.students = []
    def addStudent(self, student):
        if self.searchStudent(student.id):
            print(f"Student with ID {student.id} exists.")
        else:
            self.students.append(student)
    def remove(self, id):
        for s in self.students:
            if(s.id == id):
                self.students.remove(s)
                return True
        return False
    def searchStudent(self, id):
        for s in self.students:
            if(s.id==id):
                return s
        return None
    def updateStudent(self, id):
        for s in self.students:
            if(s.id==id):
                print("Leave blank to keep the current value.")
                name = input("Update name of student : ")
                if name:
                    s.name = name
                age = input("Update age of student : ")
                if age:
                    s.age = int(age)
                grade = input("Update grade of student : ")
                if grade:
                    s.grade = grade
                email = input("Update email of student : ")
                if email:
                    s.email = email
                print("Student Updated Successfully\n")
                return
        print(f"Student not found with Id {id}")
    def display_AllStudents(self):
        i = 1
        for s in self.students:
            print(f"Details of Student Number {i}")
            print(f"Student ID : {s.id}")
            print(f"Student Name : {s.name}")
            print(f"Student Age : {s.age}")
            print(f"Student Grade : {s.grade}")
            print(f"Student Email : {s.email}\n\n")
            i += 1
    def sort_by_Name(self):
        self.students.sort(key = lambda s:s.name)
        print("Students sorted by name")
    def sort_by_Grade(self):
        grades = {'A':85,'A-':80,'B+':75,'B':70,'C+':65,'C':60,'D+':55,'D':50,'F':49}
        self.students.sort(
            key = lambda s:grades[s.grade.upper()],
            reverse = True
            )
        print("Students sorted by grade")