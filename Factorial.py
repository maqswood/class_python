n = int(input("enter your number for factorial"))
if n < 0:
    print("entered number is not exist factorial")
elif n == 0:
    print("factorial of zero is 1 ")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("factorial of ", n, "is ", factorial)
