def sortDict(studentDict):
    sorted_students = []
    
    for name, marks in studentDict.items():
        average_marks = sum(marks) / len(marks)
        sorted_students.append((name, average_marks))
    
    sorted_students.sort(key=lambda item: item[1], reverse=True)
    
    sorted_dict = {}
    for student in sorted_students:
        sorted_dict[student[0]] = studentDict[student[0]]
    
    return sorted_dict
students = {
    "Aditya": [45, 20],
    "raj": [23, 21],
    "saha": [43, 34]
}
sorted_students = sortDict(students)
print(sorted_students)
