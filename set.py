students = [
    {"name": "joseph", "department": "computer science"},
    {"name": "olumide", "department": "computer science"},
    {"name": "sarah", "department": "English"},
    {"name": "Anuoluwapo", "department": "Economics"},
    {"name": "Victoria", "department": "Mathematics"},
]

dept = set()
for student in students:
    dept.add(student["department"])
    
for department in sorted(dept):
    print(department)