# n = int(input("请输入整数：　")) #第一种ｆｏｒ循环方法
# for i in range(1,n+1):
#     for k in range(i):
#         print("*",end="")
#     print()
  
# n = int(input("输入： "))   #while循环做
# i = 1
# while i <= n:
#     k = 1
#     while k <= i:
#         print("*",end="")
#         k = k+1
#     i = i+1
#     print()

# n = int(input("输入:"))
# for i in range(1,n+1):


# L = list(range(1,101))
# print(L)
# a = L.copy()
# B=a[0:10]
# print(B)
# A = L.copy()
# A= []
# for i in L:
#     if i % 3 ==0:
#         A.append(i)
# print(A)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{0}x{1}={2}".format(i,j,i*j),end=" ")
#     print()
# print()

# 4.将‘I am a gril’按照‘gril a am I’的格式输出



# s = "I am a gril"
# a = s.split()
# b = a[::-1]

# print("转换后为", b)


# n = int(input("请输入一个正整数: "))
# for i in range(1,n):
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for k in range(1,1+i):
#         print("*",end=" ")
#     print()
# print()


# 四、思考题
# 购物车功能要求：
# 要求用户输入总资产，例如： 2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# goods = [
# {"name":"电脑","price":1999},
# {"name":"鼠标","price":10},
# {"name":"游艇","price":20},
# {"name":"美女","price":98},
# ]
L=[]
x = {}
x["name"] = "电脑"
x["price"] = 1999
L.append(x)
y = {}
y["name"] = "鼠标"
y["price"] = 10
L.append(y)
z = {}
z["name"] = "游艇"
z["price"] = 20
L.append(z)
c = {}
c["name"] = "美女"
c["price"] = 98
L.append(c)
print(L)
print("商品\t"+" ""价格\t")
print()
for i in L:
    print(i["name"]+"\t",i["price"])
money = int(input("请输入总资产: "))
gwc = 0
while True:
    print("商品1:电脑：1999元")
    print("商品2:鼠标：10元")
    print("商品3:游艇：20元")
    print("商品4:美女：98元")
    want=int(input("请输入你想要的商品编码: "))
    if want == 1:
        gwc += 1999
        if gwc < money:
            print("购买成功")
            print("继续购买请继续输入")
        else:
            print("您的余额不足，无法购买")
            break
    elif want == 2:
        gwc += 10
        if gwc < money:
            print("购买成功")
            print("继续购买请输入")
        else:
            print("您的余额不足，无法购买")
            break
    elif want == 3:
        gwc += 20
        if gwc < money:
            print("购买成功")
            print("继续购买请输入编号")
        else:
            print("您的余额不足，无法购买")
            break
    elif want == 4:
        gwc += 98
        if gwc < money:
            print("购买成功")
            print("继续购买请输入编号")
        else:
            print("余额不足，无法购买")
            break
  

    

