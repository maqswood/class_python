num = int(input("pls enter a positive number"))
sum = 0
if num < 0:
    print("you entered a negative number")
else:
    while num > 0:
        sum += num
        num -= 1
    print("sum =", sum)
