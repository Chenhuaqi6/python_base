#raise.py
# def make_except():
#     print("开始．．．")
#     raise ValueError   #    ValueError 是类型，故意触发一个异常 
#     # e = ValueError("这是我故意制造的一个错误")
#     # raise e
#     raise ZeroDivisionError("自定义的除零错误")
#     print("结束！")
# try:
#     make_except()
# except ValueError as err:
#     print("得到make_except里发出的异常通知")
#     print("err=",err)
# # except ZeroDivisionError as err:
# #     print(err) 
# print("程序结束")

# 练习：
#     写一个函数，get_age()用来获取一个人的年龄信息，此函数的规定用户只能输入１－１４０之间的整数，
#     如果用户输入其他数据则直接触发ValueError类型错误通知

def get_age():
    n = int(input("请输入一个整数（1~140）: "))
    if n >140 or n < 1:
        raise ValueError
    return n
try:
    age = get_age()
    print("用户输入的年龄是: ",age)
except ValueError as err:
    print("用户输入的不是１－１４０之间的整数,获取年龄失败")




















