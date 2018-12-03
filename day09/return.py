#此示例示意return的用法

# def f1():
#     print(1)
#     print(2)
#     return 1
#     print(3)
# v = f1()
# print(v)
# v = f1()
# print(v)

# def mymax(a,b,c):
#     zuida = a
#     if b > zuida:
#         zuida = b
#     if c > zuida:
#         zuida = c
    
#     return zuida
# print(mymax(100,200,300))
# 方法２
# def mymax(a,b,c):
#     s=max(a,b,c)
#     return s
# print(mymax(100,200,300))
# print(mymax("ABC","abc","123"))

# def mymax2(x,y):
#     if x> y:
#         return x
#     return y
# print(mymax2(mymax2(100,200),300))


# 2、写一个函数myadd()实现给出俩个数，返回这俩个数的和


# def myadd(x,y):
#     return x+y
# a = int(input("请输入第一个数: "))
# b = int(input("请输入第二个数: "))
# print(myadd(a,b))

def input_number():
    myl = []
    while True:
        n = int(input("请输入正整数: "))
        if n < 0:
            break
        myl.append(n)
    return myl
L = input_number()
print("最大的数", max(L))
print("最小的数", min(L))
print("和是", sum(L))
