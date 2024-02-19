def sortDict(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    n = len(values)
    for i in range(n):
        for j in range(n - i - 1):
            if values[j] < values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    sorted_dict = {}
    for i in range(n):
        sorted_dict[keys[i]] = values[i]

    return sorted_dict

def main():
    dict = {}
    n = int(input("Enter the number of students: "))
    for i in range(n):
        name = input("Enter the name of the student: ")
        marks = int(input("Enter the marks of the student: "))
        dict[name] = marks
    sorted_dict = sortDict(dict)
    print(sorted_dict)

main()
