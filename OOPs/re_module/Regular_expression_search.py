import re

mystring = "welcome to python world.and use for study"
x = re.search("^welcome.*study$", mystring)
if x:
    print("there is match")
else:
    print("no match")
