names = []
#to open a file
with open("names.txt") as file:
    for line in file:
        
        names.append(line.rstrip())
        
 #to sort the names in the file in reverse form       
for name in sorted(names, reverse=True):
    print(f"hello, {name}")