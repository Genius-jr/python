class Student:
    def __init__(self, name, col):
        self.name = name
        self.col = col
    def __str__(self):
        return f"{self.name} from {self.col}"
    #getter
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name 
    @property
    def col(self):
        return self._col
    #setter
    @col.setter
    def col(self, col):
        if col not in ("COSIT", "COSMAS", "COHUM", "COSPED", "COVTED"):
            raise ValueError("invalid college")
        self._col = col
    @classmethod
    def get(cls):
        name = input("Name: ").capitalize()
        col = input("College: ").upper()
        return cls(name, col)
    
    
def main():
    student = Student.get()
    print("Brilliant Student")
    print(student)
    
    

if __name__ =="__main__":
    main()