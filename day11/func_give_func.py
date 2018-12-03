# def f1():
#     print("f1函数被调用")
# def f2():
#     print("f2函数被调用")
# def fx(fn):
#     print("fn=", fn)
#     # fn()
#     fn()
# fx(f1)
# fx(f2)
# --------------------------------------------------------------------
#看如下程序的执行结果

# def goodbye(L):
#     for x in L:
#         print("再见",x)
# def hello(L):
#     for x in L:
#         print("您好",x)
# names =["Tom","Jerry","Spike","Type"]
# def fx(fn,L):
#     fn(L)
# fx(hello,names)
# fx(goodbye,names)

def myinput(fn):
    L=[1,3,9,5,7]
    return fn(L)
print(myinput(max))
print(myinput(min))
print(myinput(sum))

# def goodbye(L):
#     for x in L:
#         print("再见",x)
# def hello(L):
#     for x in L:
#         print("你好",x)
# names=["chen","hua","qi"]
# def f1(f,L):
#     f(L)
# f1(hello,names)

def hello(L):
    for x in L:
        print("你好",x)
def goodbey(L):
    for x in L:
        print("再见",x)
def f1(f,L):
    f(L)
l = ["陈华齐","球球","yy"]
f1(hello,l)