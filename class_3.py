class Student:
    def __init__(self, name, col, course):
        if not name:
            raise ValueError("Missing Name")
        if col not in ("COSIT", "COHUM", "COSMAS","COVTED", "COSPED"):
            raise ValueError("Invalid college")
        self.name = name
        self.col = col
        self.course = course
    def __str__(self):
        return f"{self.name} from {self.col}"
    def charm(self):
        match self.course:
            case "CSC":
                return "GENIUS"
            case "ECO":
                return "Scholar"
            case _:
                return "student"

def main():
    student = get_student()
    print("Brilliant Student")
    print(student.charm())
    
def get_student():
    name = input("Name: ")
    col = input("College: ").upper()
    course = input("What's your course code: ").upper()
    return Student(name, col, course)


if __name__ =="__main__":
    main()