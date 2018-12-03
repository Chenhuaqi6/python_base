#字符串的解析


s = "hello"
L = s.split(" ")
print(L)

# L = [x**2+1 for x in range(1,10)]
# L = []
# for x in range(0, 101):
#     if x % 5 != 0:
#         L.append(x**2+1)
# print(L)


# x = int(input("请输入一个整数: "))                        
# if x < 2:
#     print(x, '不是素数')
# else:
#     prime_flag = True  # 先假设x是素数
#     for i in range(2, x):
#         if x % i == 0:  # 说明整数
#             prime_flag = False
#             break
#     # 当循环结束后,prime_flag 为真则为素数
#     if prime_flag:
#         print(x, "是素数")
#     else:
#         print(x, "不是素数")
# L = []
# flag = True
# for x in range(101):
        
#     for y in range(2,x):
#         if x % y == 0:
#             flag = False
#             break
#     if flag:
#         L.append(x)
#     else:
#         pass
# print(L)
s = input("请输入用户名: ")
m = int(input("请输入密码: "))
if s == "seven" and m ==  123:
    print("登录成功")
else:
    print("登录失败")


s = input("请输入用户名: ")
m = input("请输入密码: ")
if s == "seven" and m ==  "123":
    print("登录成功")
else:
    for i in range(1,4):
        k = 4 - i
        print("您剩余机会: ", k)
        s = input("请输入用户名: ")
        m = input("请输入密码: ")
    if s == "seven" and m ==  "123":
        print("登录成功")
    else:
        print("登录失败")
