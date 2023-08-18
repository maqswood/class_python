import re

mystr = "welcome to * luminar"
x = re.sub("\s", "*", mystr)
print(x)
# it's replaced space with "*"

x = re.sub("to", "hi", mystr)
print(x)
# it's replaced "to" to "hi"
