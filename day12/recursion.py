
# def fx(n):
#     print("递归进入第", n ,"层")
#     if n == 3:
#         return
#     fx(n+1)
#     print("递归退出第",n ,"层")
# fx(1)
# print("程序结束")



def fx(n):
    print("*"*n)
    if n == 4:
        return
    fx(n+1)
    print("*"*n)
fx(1)
print("程序结束")



#此示例示意递归思想实现阶乘

# def myfac(n):
#     #假设此函数已经实现
#     if n==1:    #我知道１的阶乘
#         return 1
#     return n*myfac(n-1)
# print(myfac(5))

def mysum(n):
    if n == 1:
        return 1
    return n+mysum(n-1)
print(mysum(100))
# print(mysum(100000))
# print(mysum(1000))
# print(mysum(100000))
