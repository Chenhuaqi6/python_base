# １、写一个函数　get_chinese_char_count(s),此函数的功能是给定一个字符串，返回这个字符串中　中文的个数
# 如：
# def get_chinese_char_count(s)：
#     ．．．
# s = input("请输入中文英文混合的字符串: ")
# print("您输入的中文个数是："，　get_chines_char_count(s))
# 注：中文字符的编码在　0x4E00-0x9FA45 之间


# def get_chinese_char_count(s):
#     myl=[]
#     for i in s:
#         if 0x4E00 < ord(i) < 0x9FA45:
#             myl.append(i)
#     return len(myl)
# s = input("请输入中文英文混合的字符串: ")
# print("您输入的中文个数是: ", get_chinese_char_count(s))


# 2. 写一个函数isprime(x) 判断x是否为素数.如果为素数
#     返回True,否则返回False
#     如:
#       print(isprime(3))  # True
#       print(isprime(4))  # False


# def isprime(x):
#     if x < 2:
#         return False
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#             break
#     else:
#         return True
# print(isprime(3))
# print(isprime(4))

# # 3. 写一个函数prime_m2n(m, n) 返回从m开始,到n结束
# #     范围内的全部素数的列表,并打印对应的列表 (不包含n)
# #     如:
# #       def prime_m2n(m, n):
# #            ...
# #       L = prime_m2n(10, 20)
# #       print(L)  # [11, 13, 17, 19]

# def prime_m2n(m,n):
#     l=[]
#     for x in range(m,n):
#         if x < 2:
#             continue
#         for i in range(2,x):
#             if x % i ==0:
#                 break
#         else:
#             l.append(x)
#     print(l)
# prime_m2n(10,20)

# def primes(n):
#     l = []
#     for x in range(n):
#         if x < 2:
#             continue
#         for i in range(2,x):
#             if x % i == 0:
#                 break
#         else:
#             l.append(x)
#             s = 0
#             for q in l:
#                 s += q
#     return l
# s = sum(primes(200))   
# l = primes(200)
# print(l,s)
结合函数：
def isprime(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
            break
    else:
        return True
        
def prime_m2n(m,n):
    L = []
    for x in range(m,n):
        if isprime(x):
            L.append(x)
    return L

def primes(n):
    return prime_m2n(0, n)
L = primes(100)
print(L)
S = primes(200)
print(sum(S))

# def myrange(*args):
#     l = []
#     if len(args) == 1:
#         i=0
#         while i < args[0]:
#             l.append(i)
#             i+=1
#     if len(args) == 2:
#         i = args[0]
#         while i < args[1]:
#             l.append(i)
#             i += 1
#     if len(args) == 3:
#         #判断步数正反
#         if args[2] > 0:
#             i = args[0]
#             while i < args[1]:
#                 l.append(i)
#                 i += args[2]+1  
#         elif args[2] < 0:
#             i = args[0]
#             while i > args[1]:
#                 l.append(i)
#                 i += args[2]


#     return l
# L = myrange(1,10,2)
# print(L)



