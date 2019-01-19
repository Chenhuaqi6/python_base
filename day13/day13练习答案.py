

import time
def mytime():
    hh=int(input("请输入小时: "))
    mm=int(input("请输入分钟: "))
    ss=int(input("请输入秒数: "))
    ss=0
    while 1:
        ss+=1
        if ss > 59:
            ss = 1
            mm += 1
        print("%d:%d:%d" % (hh,mm,ss),end='\r')
        time.sleep(0.2)
        # i+=1
   
mytime()

# import time
# while True:
#     a = time.localtime()
#     # HH=a[3]
#     # MM=a[4]
#     # SS=a[5]
#     # print("%02d:%02d:%02d" % (HH,MM,SS))
#     print("%02d:%02d:%02d" % a[3:6],end = "\r")
#     time.sleep(1)

# import time
# hh =int(input("请输入小时: "))
# mm = int(input("请输入分钟: "))
# ss = int(input("请输入秒数: "))
# while True:
#     a = time.localtime()
#     HH=a[3]
#     MM=a[4]
#     SS=a[5]
#     print(HH,":",MM,":",SS,end = "\r")
#     time.sleep(1)
#     if HH==hh and MM == mm and SS == ss:
#         print("时间到")
#         break

import math
def fun(n):
    s = 1
    for x in range(1,n+1):
        s += 1/math.factorial(x)
    return s
print(fun(500))

# n = int(input("请输入一个数: "))
# s=0
# # l=[-1]
# for x in range(n):
#     # for y in l:
#     s += ((-1)**x)/(2*(x+1)-1)
# d = s*4    
# print(s,d)





