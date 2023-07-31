students =[]
with open ("student.csv") as file:
    for line in file:
        #to split the comma and identify it differently
        name, dept = line.rstrip().split(",")
        student = {"name": name, "dept": dept}
        students.append(student)
        
def get_name(student):
    return student["name"]
#to sort by dept swap the get_name with get_dept and everything that has name with dept
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['dept']}")
    
    
