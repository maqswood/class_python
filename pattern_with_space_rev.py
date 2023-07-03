rows = int(input("enter yor number"))
k = 10
for i in range(rows, 0, -1):
    for j in range(k):
        print(end=" ")
    k = k + 2
    for x in range(i):
        print("*", end="   ")
    print()
