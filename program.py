def sortDict(studentDict):
    sortStudent = []
    
    for name, marks in studentDict.items():
        average_marks = sum(marks) / len(marks)
        sortStudent.append((name, average_marks))
    
    sortStudent.sort(key=lambda item: item[1], reverse=True)
    
    sortedDict = {}
    for student in sortStudent:
        sortedDict[student[0]] = studentDict[student[0]]
    
    return sortedDict
students = {
    "Aditya": [95, 90],
    "Raj": [83, 81],
    "Saha": [73, 74]
}
sortedStudents = sortDict(students)
print(sortedStudents)
