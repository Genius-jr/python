class Student:
    def __init__(self, name, col):
        if not name:
            raise ValueError("Missing Name")
        if col not in ("COSIT", "COHUM", "COSMAS","COVTED", "COSPED"):
            raise ValueError("Invalid college")
        self.name = name
        self.col = col
    def __str__(self):
        return f"{self.name} from {self.col}"
def main():
    student = get_student()
    print("Brilliant Student")
    print(student)
    
def get_student():
    name = input("Name: ")
    col = input("College: ").upper()
    return Student(name, col, course)


if __name__ =="__main__":
    main()