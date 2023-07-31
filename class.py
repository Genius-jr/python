class Student:
    def __init__(self, name, col):
        if not name:
            raise ValueError("Missing Name")
        if col not in ("COSIT", "COHUM", "COSMAS", "COVTED", "COSPED"):
            raise ValueError("Invalid college")
        self.name = name
        self.col = col

def main():
    student = get_student()
    print(f"{student.name} from {student.col}")
    
def get_student():
    name = input("Name: ")
    col = input("College: ").upper()
    return Student(name, col)

if __name__ =="__main__":
    main()
    
    
    
