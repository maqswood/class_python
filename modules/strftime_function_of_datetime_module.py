import datetime

x = datetime.datetime.now()

print("current date& time", x)
print("abbreviate form",x.strftime("%a"))
print("full form",x.strftime("%A"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%d"))
print(x.strftime("%D"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%Y"))
print(x.strftime("%y"))
print(x.strftime("%s"))
print(x.strftime("%S"))