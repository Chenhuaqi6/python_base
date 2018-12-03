# myinteger.py
#示例示意
class Mynumber:
    def __init__(self,value):
        self.data =value
    def __int__(self):
        """此方法用于将对象self.转为整数
        此方法必须返回函数"""
        return int(self.data)
    def __float__(self):
        return float(self.data)
n1 = Mynumber("100")
print(int(n1))
print(float(n1))
















# class MyInteger:
#     def __init__(self, value):
#         self.data = int(value)

#     def __int__(self):
#         '''此方法必须返回整数'''
#         return self.data

#     def __float__(self):
#         return float(self.data)

# a1 = MyInteger("100")
# i = int(a1)  # 将MyInteger类型转为整数
# print(i)

# f = float(a1)  # a1.__float__()
# print(f)

# c = complex(a1)  # a1.__complex__()
# print(c)

# b = bool(a1)  # a1.__bool__()
# print(b)
