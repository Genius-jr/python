students =[]
with open ("student.csv") as file:
    for line in file:
        #to split the comma and identify it differently
        name, dept, college = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["dept"] = dept
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['dept']}")