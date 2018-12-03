
#此示例示意global语句的语法和用法
# v =100
# def f1():
#     global v   #global声明v为全局变量
#     v=200　　　#想让此赋值语句去修改全局变量v
# f1()
# print("v=", v)



#４、global变量列表里的变量名不能出现在函数的形参列表里
     #函数的形参不能用global
# v =100
# def f1(v):
#     global v   #此处一定出错
#     v=200　　　#想让此赋值语句去修改全局变量v
# f1(300)
# print("v=", v)

# #练习
# 用全局变量记录一个函数hello　被调用的次数部分代码如下：
count = 0
def hello(name):
    print("您好",name)
    global count
    count += 1
hello("小张")
hello("小李")
hello("小陈")
print("hello函数被调用", count)

