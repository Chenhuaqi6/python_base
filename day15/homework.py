# s=100
# i = 0
# while i < 10:
#     s = s/2
#     i+=1
# print("第10次反弹: ", s)


# s=100
# i = 0
# l=[]
# while i < 10:
#     s = s/2
#     i+=1
#     l.append(s)
# x = 0
# for ch in l:
#     x+=ch
# long = 100+x*2
# print(long)


# 2. 分解质因数.输入一个正整数,分解质因数
#     如 输入: 90 则打印: 90=2*3*3*5
#     (质因数是指最小能被原数整除的素数(不包括1))

# l1=[]
# l2=[]
# num=n = int(input("请输入一个正整数: "))

# for x in range(n+1):
#     if x < 2:
#         continue
#     for y in range(2,x):
#         if x % y ==0:
#             break
#     else:
#         l1.append(x)

# while n!=1:
#     for z in l1:
#         if n % z ==0:
#             l2.append(z)
#             n = int(n/z)
#             break
# print(l2)
# s = [str(x) for x in l2]
# print(s)
# s1 = "x".join(s)
# print(s1)
# print("%d=%s" % (num,s1))




# def prime(begin, end):
#     for x in range(begin,end):
#         if x < 2:
#             continue
#         for y in range(2,x):
#             if x % y == 0:
#                 break
#         else:
#             yield x

# L=[x for x in prime(10, 30)]  #L=[11,13,17,19]
# print(L)


#   2. 写一个生成器函数myxrange([start, ], stop[, step]) 来生成一系列整数
#     要求:
#       myxrange功能与range功能相同（不允许调用range函数)
#     用自己写的myxrange函数结合生成器表达式求1~10内奇数的平方和

# def myrange(*args):
#     if len(args) == 1:
#         i = 0
#         while i <args[0]:
#             yield i
#             i +=1
#     if len(args) == 2:
#         i = args[0]
#         while i < args[1]:
#             yield i
#             i +=1
#     if len(args) == 3 and args[2] > 0:
#         i = args[0]
#         while i < args[1]:
#             yield i
#             i+=1+args[2]
#     if len(args) == 3 and args[2] < 0:
#         i =args[0]
#         while i > args[1]:
#             yield i
#             i += args[2]
# l = [x for x in myrange(1,10,2)]
# print(l)
# l=[]
# for x in myrange(100):
#     if x % 2 == 1:
#         l.append(x)
# print(l)
# s = 0
# for y in l:
#     s += y**2
# print(s)

# l=[]
# for x in range(1,1000):
#     for y in range(1,x):
#         if x % y == 0:
#             l.append(y)
#     if sum(l)==x:
#         print(l)
#         print(x)
#     l=[]


# l = []
# for x in range(1,1000):
#     for y in range(1,x):
#         if x % y == 0:
#             l.append(y)
#     if sum(l) == x:
#         print(l)
#         print(x)
#     l=[]