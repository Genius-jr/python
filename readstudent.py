students =[]
with open ("student.csv") as file:
    for line in file:
        #to split the comma and identify it differently
        row = line.rstrip().split(",")
        #you can also use name, house = line.rstrip().split(",") to split and the print will be name and house
        students.append(f"{row[0]} is in {row[1]} department")
for student in students:
    print(student)