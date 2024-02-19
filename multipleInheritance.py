class University:
    def __init__(self, name):
        self.name = name

    def university(self):
        return f"University Name: {self.name}"
    
    class Department:
        def __init__(self, name, head):
            self.name = name
            self.head = head

        def department(self):
            return f"Department Name: {self.name}, Department Head: {self.head}"

        class Student:
            def __init__(self, name, roll_no):
                self.name = name
                self.roll_no = roll_no

            def student(self):
                return f"Student Name: {self.name}, Roll No: {self.roll_no}"
            
university = University(name="Jharkhand University")
department = University.Department(name="Computer Science", head="Dr. Manoj Kumar")
student = University.Department.Student(name="Aditya", roll_no="12204244")

print(university.university())
print(department.department())
print(student.student())