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

# def tri_recursion(k):
#     if (k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)
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


# def myfunc():
#     x = 300
#
#     def myinnerfunc():
#
#         print(x)
#
#     myinnerfunc()
#
#
# myfunc()


# x = 300
#
# def myfunc():
#     x=400
#     print(x)
#
# myfunc()
#
# print(x)

#
#
# import platform
#
# x = platform.system()
# print(x)
#
# import platform
#
# x = dir(platform)
# print(x)
# import camelcase
#
# x = camelcase.CamelCase()
# txt = "maqswood is king"
# print(x.hump(txt))


# import sys
# import matplotlib
#
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import numpy as np
#
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
#
# plt.plot(xpoints, ypoints)
# plt.show()
# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()




