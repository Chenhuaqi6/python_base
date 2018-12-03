# def power2(x):
#     print("power2被调用",x)
#     return x ** 2
# #生成一个可迭代对象，此可迭代可以生成１－９的整数的平方

# for i in map(power2,[1,2,3,4,5,6,7,8,9]):
#     print(i)


# def mypower2(x,y):
#     return x ** y
# for i in map(mypower2,range(1,5),range(4,0,-1)):
#     print(i)

# for x in map(pow,[1,2,3,4],[4,3,2,1],range(5,10)):
#     print(x)


# def mysub1(x):
#     return x**2
# s = 0
# for x in map(mysub1,range(1,10)):
#     s += x
# print(s)
# print(sum(map(lambda n:n**2,range(1,10))))
# print(sum(map(lambda n:n**3,range(1,10))))
# print(sum(map(pow,range(1,10),range(9,0,-1))))

# def mysub2(x):
#     return x**3
# s = 0
# for x in map(mysub1,range(1,10)):
#     s += x
# print(s)

# def mysub3(x,y):
#     return x**y
# s = 0
# for x in map(mysub3,range(1,10),range(9,0,-1)):
#     s += x
# print(s)

# for x in filter(lambda x:x%2,range(11)):
#     print(x)

# l=[5,-2,-4,0,3,1]
# l2=sorted(l) #l2=[-4,-2,0,1,3,5]
# l3 = sorted(l,reverse=True) #降序
# l4 = sorted(l,key=abs)
# print(l4)


# def mynames(x):
#     return x[::-1]
# print(mynames("chen"))

mysub = sum(map(lambda x,y:x**y,range(1,5),range(5,1,-1)))
print(mysub)



