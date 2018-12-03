#　此示例示意位置传参
# def myfun(a,b,c):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# l = [3,4,5]
# myfun(*l)


# def myfun(a,b,c):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# myfun(c=33,b=22,a=11)



# def myfun(a,b,c):
#     print("a=",a)
#     print("b=",b)
#     print("c=",c)
# d={"a":100,"c":300,"b":200}
# myfun(**d)


# 练习:
#     写一个函数，传入三个参数，返回这三个参数中的最大值元素和最小值元素　
#     结果要去：形成元组最小值在前　最大值在后返回给调用者
# def minmax(a,b,c):
#     return(min(a,b,c),max(a,b,c))
# t=minmax(300,200,100)
# print(t)

# def info(name,age=1,address="不详"):
#     print(name,"今年",age,"岁，家庭住址：",address)
# info("陈华齐",21,"郑州")
# info("陈华齐",15)
# info("陈华齐")


# 练习：
# 　　写一个函数，myadd，此函数可以传入二个，三个，或四个实参
# 　　此函数的功能是计算所有实参的和
# 如：
#     def myadd(...):
#         ...
#     print(myadd(10,20)) #30
#     print(myadd(100,200,300)) #600
#     print(myadd(1,2,3,4)) # 10


# def myadd(a,b=0,c=0,d=0):
#     s = a+b+c+d
#     return s
# print(myadd(100,200,300,400))
# print(myadd(100,200))
# print(myadd(100))

# def myadd(a,b=0,c=0,d=0):
#     s = a+b+c+d
#     return s
# print(myadd(100,200,300,400))
# print(myadd(100,200))
# print(myadd(100))


#在函数内部对变量赋值是在函数内部创建新的局部变量
#此赋值语句不会改变外部变量的绑定关系
# L = [1,2,3]
# def f1(L):
#     L = [4,5,6]
#     print(L) #[4,5,6]
# f1(L)
# print(L) #[1,2,3]

# L = [1,2,3]
# def f1(L):
#     # L = [4,5,6]
#     L.append("ABC")
#     print(L) #[1,2,3,"ABC"]
# f1(L)　
# print(L) #[1,2,3,"ABC"]

#面试题
#试运行一下程序的结果是什么，为什么？
# L = [1,2]
# def fn(a,lst=[]):
#     lst.append(a)
#     print(lst)
# fn(3,L)
# print(L) 
# fn(4,L)
# print(L)
# fn(5)

# fn(6)

# fn(7)



# L = [1,2]
# def fn(a,list=None):
#     if list is None:
#         list=[] #新创建全新的列表
#     list.append(a)
#     print(list)
# fn(3,L) 
# fn(4,L)
# fn(5)
# fn(6)
# fn(7)



# def mydict(**kwargs):
#     return kwargs
# d = mydict(name="Lucy",age=200,number=1)
# print(d)
# def func(*args):
#     print("实参的个数：",len(args))
#     print("arg=",args)
# func() #无参
# func(1,2,3,4)
# s = "abcde"
# func(*s) #等同于func("a","b","c","d","e")

# def mysum(*args):
#     return sum((args))
# s = [1,2,4,]
# print(mysum(*s))

# def mysum(*args):
#     s = 0
#     for x in args:
#         s += x
#     return s
#     # return sum((args))
# n = [1,2,3,4]
# print(mysum(*n))
# print(mysum(1,2,3,4))
# def func(a,b,*,c,d):
#     print(a,b,c,d)
# func(1,2,c=10,d=20)
#  * 后面的都要是关键字传参

# 练习　
# 　　已知内建函数　max 的帮助文档为：
#     max(...)
#       max(iterable) ---->value
#       max(args1,args2,*args) ---->value
#    仿造max函数，写一个与max功能完全一样的mymax函数
#    （要求:不允许调用内建的ｍａｘ函数）
# def mymax(...):

# print(mymax([6,8,3,5])) #8
# print(mymax(100,200)) #200
# print(mymax()) #报错


def mymax(a,*args):
    
    if len(args) == 0:  #判断是否是一个参数
        zuida=a[0]
        for x in a:
            if x > zuida:
                zuida = x
    else:
        zuida = a
        for x in args:
            if x > zuida:
                zuida = x
    return zuida
    
print(mymax([6,8,3,5]))
print(mymax(1,2,3,4,5))
#a 只存储一个　１　剩下的都在args中　遍历args中的值与a 进行比较



#此示例示意双星号字典形参

# def func(**kwargs):
#     print("关键字传参的个数: ",len(kwargs))
#     print("kwargs=",kwargs)
# func(name="魏老师",age=35,address="朝阳")

def func(**kwargs):
    print("关键字传参的个数: ",len(kwargs))
    print("kwargs=",kwargs)
func(a=1,b=2,name="魏老师",age=35,address="朝阳")
    
func(a=1,b=2,c=3)