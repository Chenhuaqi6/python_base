# 打印　１　－２０　的整数，打印在一行内

# j = 1
# while j <= 10:
#     j += 1
#     i = 1
#     while i <= 20:
#         print(i,end=" ")
#         if i == 10:
#             break
#         i += 1
#     print()



# 练习：
# 　输入一个整数ｎ　打印指定宽度的正方形

# n = int(input("请输入一个整数: "))
# j = 1
# while j <= n:
#     i = 1
#     while i <= n:
#         print(i,end=" ")
#         i += 1
#     print()
#     j += 1


# i = 1
# while i <= 20:
#     print(i, end=" ")
#     if i % 5 == 0:
#        print()
#     i += 1

# i = 10
# while i > 0:
#     print(i,end=" ")
    
#     i -= 1

# i = 0.0
# while i < 10:
#     print(i)
#     i += 0.5

# s = 0
# i = 1
# while i <=100:
#     s += i
#     i += 1
# print(s)

# begin = int(input("请输入开始值: "))
# end = int(input("请输入结束值: "))
# i = begin
# count = 0
# while end > i:
#     print(i,end=" ")
#     count += 1 
#     if count == 5:
#         print()
#         count = 0
#     i += 1
# else:
#     print()


# s = 0
# while True:
#     x = int(input("请输入一个正整数：　"))
#     if x < 0:
#         break
#     s += x
# print(s)
    
s = 0
while True:
    i = int(input("请输入一个正整数: "))
    if i < 0:
   
        break
    s += i  
print(s)