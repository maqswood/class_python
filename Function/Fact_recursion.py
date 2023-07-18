def fact_recursion(n):
    if n == 1:
        return n
    else:
        return n * fact_recursion(n - 1)


num = int(input("enter a number"))
if num < 0:
    print("not valid for factorial")
elif num == 0:
    print("factorial of 0 is 1")
else:
    print("Your result of", num, "is", fact_recursion(num))
