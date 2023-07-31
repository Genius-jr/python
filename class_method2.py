import random
class Hat:
    
    houses = ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin")
    @classmethod
    def sort(cls, name):
        print(name,"is in", random.choice(cls.houses))
    
    
    
name = input("What's your name? ").capitalize()
Hat.sort(name)