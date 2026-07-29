class Validator:
    def validate_age(self, age):
        if isinstance(age, int) and (0<age<=100):
            return True
        return False
    def validate_email(self, email):
        if email.count("@")!= 1:
            return False
        username, domain = email.split('@')
        if username == "":
            return False
        elif domain == "":
            return False
        elif '.' not in domain:
            return False
        else:
            return True
    def validate_grade(self, grade):
        valid_grades = {'A':85,'A-':80,'B+':75,'B':70,'C+':65,'C':60,'D+':55,'D':50,'F':49}
        if grade.upper() in valid_grades:
            return True
        return False
    def validate_id(self, id):
        return id.isdigit() and len(id)==8
    def validate_name(self, name):
        return (name.replace(" ","").isalpha())