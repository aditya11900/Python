class Student:
    def __init__(self, name):
        self.name = name

class StudentB(Student):
    def __init__(self, name, grade):
        super().__init__(name) 
        self.grade = grade
        
student_b = StudentB(name="Aditya", grade="A")
print("Name:", student_b.name)
print("Grade:", student_b.grade)
 