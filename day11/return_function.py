#return_function.py

# def f1():
#     print("f1")
# def f2():
#     print("f2")
# def get_fx(n):
#     if n==1:
#         return f1
#     elif n == 2:
#         return f2
# fx= get_fx(1)
# fx()   #调用f1
# fx=get_fx(2)
# fx()    #调用f2



# def get_function():
#     s = input("请输入操作: ")
#     if s == "求最大":
#         return max
#     elif s == "求最小":
#         return min 
#     elif s == "求和":
#         return sum
# l = [2,4,6,8,7,9]
# fx = get_function()
# v = fx(l)
# print(v)


def myadd(x,y):
    return x+ y
def mysub(x,y):
    return x-y
def mymul(x,y):
    return x*y

def get_func(s):
    # s = input("请输入您的操作: ")
    if s == "+" or s == "加":
        return myadd
    elif s == "-"or s =="减":
        return mysub
    elif s == "*" or s == "乘":
        return mymul
# fx = get_func()
# v = fx(1,5)
# print(v)

def main():
    while True:
        s = input("请输入计算公式: ")
        L=s.split(' ')
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print("结果是: ", fn(a,b))
main()