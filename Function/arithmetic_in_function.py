def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    return x / y


print("pls enter your choice")
print("A.addition")
print("B.subtraction")
print("C.multiplication")
print("D.division")
choice = input("enter your choice")
num1 = int(input("enter your first number"))
num2 = int(input("enter your second number"))

if choice == "a" or choice == "A":
    print("result=", add(num1, num2))
elif choice == "b" or choice == "B":
    print("result=", sub(num1, num2))
elif choice == "C" or choice == "c":
    print("result=", mult(num1, num2))
elif choice == "D" or choice == "d":
    print("result=", div(num1, num2))
else:
    print("invalid choice")
