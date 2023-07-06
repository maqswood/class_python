First_number = int(input("enter your first number"))
Second_number = int(input("enter your second number"))
Third_number = int(input("enter your third number"))
if First_number > Second_number and First_number > Third_number:
    print(First_number, " is larger")
elif Second_number > First_number and Second_number > Third_number:
    print(Second_number, "is larger")
else:
    print(Third_number, " is larger")
