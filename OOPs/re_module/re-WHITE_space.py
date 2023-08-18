import re

mystr = "welcome to luminar"
x = re.search("\s", mystr)
print("space location is ", x.start())
