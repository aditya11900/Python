class Student:
    def __init__(self, m):
        self.marks = m

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student(100)
s2 = Student(100)

if s1 == s2:
    print("Both students have equal marks.")
else:
    print("Both students have different marks.")