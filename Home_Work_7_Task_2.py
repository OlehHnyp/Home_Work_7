import re


password =  input("Enter password:")

if (    re.search('[a-z]', password)
    and re.search('[A-Z]', password)
    and re.search('[0-9]', password)
    and re.search('[$#@]', password)
    and len(password) > 5
    and len(password) < 17):
    print("Password is valid")
else:
    print("Password is not valid")


