#练习
# n = int(input("请输入一个整数: "))
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print("*",end="")
#         j += 1
#     print()
#     i += 1

# n = int(input("输入一个数:"))
# for i in range(n+1):
#     for k in range(n-i):
#         print("*",end=" ")
#     print()

# n = int(input("输入一个数：　"))
# i = 1
# while i<=n:
#     k = 1
#     while k <= n-i:
#         print("*",end=" ")
#         k += 1
#     print()
#     i+=1

# n = int(input("请输入一个整数: "))
# i = 1
# while i <= n:
#     k = n -i
#     print(" " * k + "*" * i)
#     i = i +1



# n = int(input("请输入一个数: "))
# if n == 2:
#     print("这个数是质数")
# else:
#     for x in range(2,n):
#         if n % x == 0:
#             print("不是质数")
#             break
#     else:
#         print("是质数")


# n = int(input("输入"))
# for i in range(1,n+1):
#     for x in range(ｉ,ｉ+n):
#         print(x,end=" ")
#     print()



# n = int(input("请输入一个正整数: "))
# for i in range(1,n+1):
#     print("*"*i)
#   *
#   **
#   ***



# n = int(input("请输入一个正整数: "))
# for i in range(1,n+1): 
#     k = n - i
#     print(' ' * k + "*" * i)
#   *
#  **
# ***



# n = int(input("请输入一个正整数: "))
# for i in range(1,n+1):
#     print( "*" * (n+1-i))
#     ***
#     **
#     *


# n = int(input("请输入一个正整数: "))
# for i in range(1,n+1):
#     print(" " * (i-1) + "*" *(n+1-i) )
#      ***
#       **
#        *

# n = int(input("请输入一个正整数: "))
# for i in range(n,0,-1):
#     print("*"*i)