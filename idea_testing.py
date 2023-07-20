# # print("enter ur 1st number")
# # x = int(input())
# # print("enter ur 2nd number")
# # y = int(input())
# #
# # add = x + y
# # sub = x - y
# # print("ur sum is ", add)
# #
# # print("ur subtraction is ", sub)
# #
# # x = 26
# # print("using and operator:x<20 and x>25=", 20 > x > 25)
# # print("using or operator:x<20 or x>25  =", x < 20 or x > 25)
# # print("using not operator:not(x<20)    =", not (x < 20))
#
# rows = int(input("enter yor number"))
# k = 2 * rows
# for i in range(rows):
#     for j in range(k):
#         print(end=" ")
#     k = k - 2
#     for x in range(i + 1):
#         print("*", end="   ")
#     print()
# for i in range(rows+1, 0, -1):
#     for j in range(k):
#         print(end=" ")
#     k = k + 2
#     for x in range(i):
#         print("*", end="   ")
#     print()


# length = int(input("enter your length"))
# list=[]
# print("enter wanted list components")
# for index in range(length):
#     n=input()
#     list.insert(index,n)
#
#
# print(list)

def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
#
# def recursion(k):
#     print(k)
#     if k > 0:
#         result = k + recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# print("recurtion result is:", recursion(6))
