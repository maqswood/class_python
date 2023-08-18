import re

mystr = "welcome to * luminar"
x = re.split("\s", mystr)
print(x)
# it's separated by space

x = re.split("\*", mystr)
print(x)
# it's separated by "*"
x = re.split("to", mystr)
print(x)
# it's separated by "str"
