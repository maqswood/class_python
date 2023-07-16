rows = int(input("enter yor number"))
k = 2 * rows
for i in range(rows):
    for j in range(k):
        print(end=" ")
    k = k - 2
    for x in range(i + 1):
        print("*", end="   ")
    print()

