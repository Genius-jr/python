import re

email = input("what's your email? ").strip().lower()
##the domain can be domain.endswith and 
#username, domain = email.split("@")
#if username and "." in domain:
#    print("valid")
#else:
#    print("invalid")
##'.' is used to represent any character except a newline while '+' is used to represent 1 or more repitition
#if re.search("..*@..*", email, re.IGNORECASE):
if re.search(r"^(\w|\.)+@(\w+\.)*\w+\.(com|edu|ng|net)$", email):
    print("valid")
else:
    print("invalid")