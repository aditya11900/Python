class Student:
    def __init__(self, name):
        self.name = name

class StudentB(Student):
    def __init__(self, student_name, grade):
        Student.__init__(self, student_name)
        self.grade = grade

student_b = StudentB(student_name="Aditya", grade="A")
print("Name:", student_b.name)
print("Grade:", student_b.grade)
