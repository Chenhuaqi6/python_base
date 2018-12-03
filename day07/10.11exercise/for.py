#for.py
#此示例示意for语句的用法


# s = "ABCDE"
# for ch in s:
#     print("ch---->", ch)
#     if ch == "C":
#         break
# else:
#     print("for语句的else子句被执行")
# print("程序结束")


# 练习
#   任意输入一段字符串
#   　１、计算出字符串中空格的个数
#   ２、　计算书字符串中　中文的个数

s = input("请输入一段字符串: ")
i = 0
q = 0
for x in s:
    if x == " ":
        i += 1
    elif ord(x)> 128:
        q += 1
print("空格的个数为",i)
print("中文的个数为: ",q)


     

# n = int(input("请输入一个整数: "))
# j = 1
# while j <= n:
#     i = j 
#     while i <= n+j-1:
#         print(i,end=" ")
#         i += 1
#     print()
#     j += 1
# n = int(input("请输入一个整数: "))

# s = 1
# while s <= n:
#     print(s,end=" ")
#     s += 1
# print()   
# s = 2
# while s <= n+1:
#     print(s,end=" ") 
#     s += 1
# print()
# s = 3
# while s <= n+2:
#     print(s,end=" ") 
#     s += 1
# print()
# s = 4
# while s <= n+3:
#     print(s,end=" ") 
#     s += 1
# print()
# s = 5
# while s <= n+4:
#     print(s,end=" ") 
#     s += 1
# print()


