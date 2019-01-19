# 示意装饰器函数的定义方式及装饰器来装饰另一个函数的语法
# def mydeco(x):
#     def fx():
#         print("++++++++++++++++++++++")
#         x()
#         print("----------------------")
#     return fx 
# # @mydeco       #等同于 myfunc=mydeco(myfunc)
# def myfunc():
#     """此函数将作为被装饰函数"""
#     print("myfunc被调用")

# #原理是让myfunc重新绑定mydeco返回回来的函数
# q=mydeco(myfunc)

# q()
# myfunc()
# myfunc()


# def mydeco(x):
#     def fx():
#         print("++++")
#         x()
#         print("----")
#     return fx

# def fun():
#     print("fun被调用")
# fun=mydeco(fun)
# fun()
# fun()

# def myfunc(y):
#     def fx(z,w):
#         print("装饰函数",z,w)
#         y(z,w)
#         print("装饰函数",z,w)
#     return fx



# @myfunc
# def myfun(z,w):
#     print("这是被装饰的函数",z,w)

# # myfun = myfunc(myfun)
# myfun(5,10)

import time
a = time.time()
def decorator(fn):
        def fun():
            print(time.time()-a)
            fn()
        return fun

@decorator
def k():
    print("被调用")

k()