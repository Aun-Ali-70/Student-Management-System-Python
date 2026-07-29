class Student:
    def __init__(self, id, name, age, grade, email):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade.upper()
        self.email = email.strip()
    def display(self):
        print(f"Student ID : {self.id}")
        print(f"Student Name : {self.name}")
        print(f"Student Age : {self.age}")
        print(f"Student Grade : {self.grade}")
        print(f"Student Email : {self.email}\n")
    def update_Name(self, newName):
        self.name = newName
    def update_Grade(self, newGrade):
        self.grade = newGrade
    def to_dict(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "age" : self.age,
            "grade" : self.grade,
            "email" : self.email
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data["id"],
            name = data["name"],
            age = data["age"],
            grade = data["grade"],
            email = data["email"]
        )