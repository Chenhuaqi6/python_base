#此示例示意闭包的定义及调用

# def make_power(y):
#     def fn(x):
#         return x**y
#     return fn 
# pow2 = make_power(2)
# print("5的平方", pow2(5))
# pow3 = make_power(3)
# print("6的立方", pow3(6))

#此示例用闭包来创建一元二次方程的函数
# def get_fx(a,b,c):
#     def fx(x):
#         return a*x**2 + b*x + c
#     return fx
# f123 = get_fx(1,2,3)
# print(f123(20))
# print(f123(50))
# f456= get_fx(4,5,6)
# print(f456(20))
# print(f456(60))


# def get_funs(n):
#     L=[]
#     for i in range(n):
#         L.append(lambda x:x*i)
#     return L
# funs = get_funs(4)
# print(funs[0](10))
# print(funs[1](10))
# print(funs[2](10))
# print(funs[3](10))


