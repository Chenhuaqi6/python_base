
#此示例示意覆盖的语法

# class A:
#     def work(self):
#         print("A.work被调用！")


# class B(A):
#     def work(self):
#         """此方法会覆盖父类中同名的方法"""
#         print("B.work被调用")
#     pass

# b = B()
# b.work()


#此示例示意显示调用父类的被覆盖方法
class A:
    def work(self):
        print("A.work被调用！")


class B(A):
    def work(self):
        """此方法会覆盖父类中同名的方法"""
        print("B.work被调用")
    pass

b = B()
A.work(b) #借助于类来调用父类方法