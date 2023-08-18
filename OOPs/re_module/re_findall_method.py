import re

mystring = "welcome to python world.and use for study"
x = re.findall("o", mystring)
print(x)
print(len(x))
