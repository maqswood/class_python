def calculate_Lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater = greater + 1
    return lcm


num1 = int(input("enter your first number"))
num2 = int(input("enter your second  number"))
print("LCM= ", calculate_Lcm(num1, num2))
