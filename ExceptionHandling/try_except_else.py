try:
    x = int(input("enter your first number"))
    y = int(input("enter your second number"))
    print(x / y)
except:
    print("Division by zero")
else:
    print("successfully completed")