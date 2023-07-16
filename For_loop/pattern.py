# n = int(input("enter your rows"))
n = range(int(input("enter your rows")))
for i in n:
    for j in range(i + 1):
        print(j, end=" ")
    print()
