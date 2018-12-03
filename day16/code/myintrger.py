#myinteger.py

#生成从０到n的整数（不包含n）

# def myinteger(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1
# for x in myinteger(300):
#     print(x)
# L = [x for x in myinteger(100)]
# print(L)
# for x in myinteger(100):
#     print(x)
# l = [x*2 for x in myinteger(10)]
# print(l)


# def myevent(start,stop):
    
#     while start < stop:
#         if start % 2 == 0:
#             yield start
#         start += 1
# for x in myevent(10,20):
#     print(x,end=" ")


def myevent(start,stop):
    if start % 2 == 1:
        start +=1
    for i in range(start,stop,2):
        yield i
for x in myevent(11,20):
    print(x,end=" ")


# def myfactorial(n):
#     s = 1  # 用来保存阶乘
#     for x in range(1, n + 1):
#         s *= x
#         yield s
# L = list(myfactorial(5))  # L = [1, 2, 6, 24, 120]
# print(L)

# print(sum(myfactorial(5)))



# l = [2,3,5,7]
# # l1=[]
# l1=[y for y in (x**2+1 for x in l)]
#     # l1.append(y)
# print(l1)

# def mylit(a):
#     for x in a:
#         yield x**2+1
# for x in mylit(l):
#     print(x)

# for y in (x**2+1 for x in l):
#     print(y)


# def mymap(fn,s):
#     for x in s:
#         yield fn(x)
# for x in mymap(lambda x:x**2,range(1,5)):
#     print(x)

def myfilter(fn,args):
    for x in args:
        if fn(x) == True:
             yield x
for x in myfilter(lambda x:x % 2==1,range(10)):
    print(x)
for x in filter(lambda x:x % 2 ==1,range(11)):
    print(x)
# l = [2,3,5,7]
# a = [x*10 for x in l]
# it =iter(a)
# print(next(it))
# l[1]=333
# print(next(it))

# l = [2,3,5,7]
# a = (x*10 for x in l)  #每进行一步要一次
# it =iter(a)
# print(next(it))
# l[1]=333
# print(next(it))


