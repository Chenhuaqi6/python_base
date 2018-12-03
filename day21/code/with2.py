#此示例示意将自定义的类变为环境管理器
#让自定义的类创建的对象能用在while语句中


class A:
    def __enter__(self):

        print("A类对象已进入with语句")
        return self
    def __exit__(self,e_type,e_value,e_tb):
        '''e_type绑定异常类型，没有异常时绑定None
            e_value绑定错误对象，没有异常时绑定None
            e_tb绑定追踪对象，没有异常时绑定None'''
        print("A类对象已经离开wirh语句")
        if e_type is None:
            print("我是没有异常时退出with语句的")
        else:
            print("我是有异常退出with语句的")
            print(e_type)
            print(e_value)
            print(e_tb)
with A() as a:
    print("这是with语句内部的第一条语句")
    int(input("请输入"))

print("程序正常退出")



# class A:
#     '''此类的对象将可用于with语句中'''
#     def __enter__(self):
#         print("已经进入到了with语句的内部")
#         return self  #把自己返回由as 来绑定
#     def __exit__(self, e_t, e_v, e_tb):
#         ''' e_t 用来绑定异常类型
#             e_v用来绑定异常对象
#             e_tb_用来绑定追踪对象
#             在没有异常时,三个形参都绑定None
#         '''
#         if e_t is None:
#             print("已正常离开with语句")
#         else:
#             print("是在出现异常时走异常流程离开的with语句")

# with A() as a:
#     print('这是with语句内部的print')
#     int(input("请输入整数: "))
