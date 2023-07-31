students =[]
with open ("student.csv") as file:
    for line in file:
        #to split the comma and identify it differently
        name, dept, college = line.rstrip().split(",")
        student = {"name": name, "dept": dept, "college": college}
        students.append(student)
        
#to sort by dept swap the get_name with get_dept and everything that has name with dept
for student in sorted(students, key= lambda student: student["dept"], reverse=True):
    if college == ("COSIT"):
        print(f"{student['name']} is brilliant because he is from {student['dept']}")
    else:
        print(f"{student['name']} is in {student['dept']}")