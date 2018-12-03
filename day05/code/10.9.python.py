# 练习:
#   1. 输入三行文字，让这三行文字在一个方框 内居中显示
#   如输入:
#      hello!
#      I'm studing python!
#      I like python!
#   显示如下:
#      +---------------------+
#      |        hello!       |
#      | I'm studing python! | 
#      |    I like python!   |
#      +---------------------+
#   2. 用while循环打印 1 ~ 20 的整数(可以打印多行)   
#   3. 用while循环打印 1 ~ 20 的整数，打印在一行显示
#     每个数字之间用一个空格分隔
#      1 2 3 4 5 6 .... 18 19 20
#   4. 用while循环打印 1 ~ 20的整数，每行打印5个，
#      打印4行,如:
#      1 2 3 4 5
#      6 7 8 9 10
#      ...
#  
#     如:
#       请输入: 6
#     打印:
#       ######
#       #    #
#       #    #
#       #    #
#       #    #
#       ######

# a = input("请输入第1行: ")
# b = input("请输入第2行: ")
# c = input("请输入第3行: ")
# x = len(a)
# y = len(b)
# z = len(c)
# max = x
# if y > max:
#     max = y
# if z > max:
#     max = z
# print("+" + "-" * (max+2) + "+")
# print("| " + a.center(max) + " |")
# print("| " + b.center(max) + " |")
# print("| " + c.center(max) + " |")
# print("+" + "-" * (max+2) + "+")



# i = 1
# while i <= 20:
#     print(i,end = "  ")
#     i += 1


# i = 1
# while i <= 1000000:
#     print(i,end=" ")
#     if i % 5 == 0:
#         print()
#     i += 1

#  5. 输入一个整数n,打印一个宽度和高度都为n个字符的长方形
#     如:
#       请输入: 4
#     打印:
#       ####
#       #  #
#       #  #
#       ####

n = int(input("请输入一个整数: "))
h = 1
print("#"*n)
while h <= n - 2:
    print("#" + " " * (n-2) + "#")
    h += 1
print("#"*n)

# x = 1
# y = 1
# while x <= 9:
#     x += 1
#     while y <= 9:
#         y += 1
#         print(x,"x",y,"=",x*y, end=" ")
        
#     else:
#         print()
#         y += 1
# i=0
# j=0
# while i<9:
#     i+=1
#     while j<9:
#         j+=1
#         print(j,"x",i,"=",i*j,"\t",end="")
#         if i==j:
#             j=0
#             print("")
#             break
