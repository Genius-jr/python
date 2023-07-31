import csv

students = []

with open("student.csv") as file:
    reader = csv.DictReader(file)
    for name, dept  in reader:
        students.append({"name": name, "dept": dept})

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['dept']}")