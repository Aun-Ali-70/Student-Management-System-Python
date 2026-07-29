class ReportManager:
    def __init__(self, students):
        self.students = students
    def highest_grade(self):
        if not self.students:
            print("No students available")
            return
        grades = {'A':85,'A-':80,'B+':75,'B':70,'C+':65,'C':60,'D+':55,'D':50,'F':49}
        highest = max(
            self.students,
            key = lambda s:grades[s.grade.upper()]
        )
        print("\nStudent with highest grade : ")
        highest.display()
    def lowest_grade(self):
        if not self.students:
            print("No students available")
            return
        grades = {'A':85,'A-':80,'B+':75,'B':70,'C+':65,'C':60,'D+':55,'D':50,'F':49}
        lowest = min(
            self.students,
            key = lambda s:grades[s.grade.upper()]
        )
        print("\nStudent with lowest grade")
        lowest.display()
    def count_students(self):
        return len(self.students)
    def average_grade(self):
        if not self.students:
            print("No students available")
            return
        grades = {'A':85,'A-':80,'B+':75,'B':70,'C+':65,'C':60,'D+':55,'D':50,'F':49,}
        value = 0
        for s in self.students:
            value += grades[s.grade.upper()]
        return value/len(self.students)
    def students_statistics(self):
        if not self.students:
            print("No students available")
            return
        print("_________ Students Statistics _________\n")
        print(f"Total Students : {self.count_students()}\n")
        print(f"Average Grade : {self.average_grade():.2f}\n")
        self.highest_grade()
        self.lowest_grade()