n = int(input("enter a number"))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
else:
    print("number is not valid for prime number")
