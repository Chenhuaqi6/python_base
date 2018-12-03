# n = float(input("请输入半径: "))
# import math
# print(math.pi*n**2)


# n = float(input("请输入圆的面积: "))
# import math
# print(math.sqrt(n/math.pi))



# def fx(n):
#     print("*"*n)
#     if n == 4:
#         return
#     fx(n+1)
#     print("*"*n)
# fx(1)
# print("程序结束")

# import time
# n = (1,9,9,7,0,3,1,7,0)
# a = tuple(n)
# b = time.mktime(a)

# print(b)
import time
y = int(input("请输入您出生的年："))
m = int(input("请输入您出生的月："))
d = int(input("请输入您出生的日："))
#形成元组
t = (y,m,d,0,0,0,0,0,0)
#算出出生时新纪元的秒数
birth_time = time.mktime(t)
#算出当前时间的秒数
current_time=time.time()
#算出　出生多少秒
second = current_time - birth_time
#算出出生天数
day = second/60/60/24
print("您已出生",day,"天")

t2=time.localtime(birth_time)
w=t2[6]
d ={
    0:"周一",
    1:"周二",
    2:"周三",
    3:"周四",
    4:"周五",
    5:"周六",
    6:"周末"
}

print("你出生在: ",d[w])