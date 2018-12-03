# n = int(input("请输入一个整数: "))
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         # if i == 1 or i ==n or k ==1 or k== i:
#         print("* ",end="")
#         # else:
#         #     print("11",end="")
#     print()
# print()


# for i in range(1,3):
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(3,0,-1):
#     for k in range(1,1+i):
#         print("*",end=" ")
#     print()
# print()

# n = int(input("sr"))
# for i in range(1,n+1):
#     for k in range(1,n+2-i):
#         print("*",end="")
#     print()

# n = int(input("sr"))
# for i in range(1,5):
#     for j in range(1,3):
#         print(" ",end="")
#     for k in range(1,2):
#         print("*",end="")
#     print()


# for i in range(1,10):
#     for y in range(i):
#         print("*",end="")
#     print()


for i in range(1,10):
    for j in range(i):
        print("{}x{}={}".format(i,j,i*j),end=" ")
        print()
print()


