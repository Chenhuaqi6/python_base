#此示例示意nonlocal语句的用法

# v = 100
# def f1():
#     v= 200
#     print("f1.v=", v)
#     def f2():
#         v =300
#         print("f2.v=", v)
#     f2()
#     print("f1.v= ", v)
# f1()
# print("全局的v=", v)

# f1.v= 200
# f2.v= 300
# f1.v=  200
# 全局的v= 100


v = 100
def f1():
    v= 200
    print("f1.v=", v)
    def f2():
        nonlocal v
        v =300      #走到此步 v = 200 变为　ｖ＝　３００
        print("f2.v=", v)
    f2()
    print("f1.v= ", v)  #此处在print v 就是　ｖ＝　３００
f1()
print("全局的v=", v)