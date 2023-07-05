start_value = int(input("enter your starting value"))
end_value = int(input("enter your ending value"))
for i in range(start_value, end_value + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
