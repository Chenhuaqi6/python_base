# mynumber.py

# 此示例示意 运算符重载
class MyNumber:
    '自定义数字'
    def __init__(self, value):
        self.data = value

    def __repr__(self):
        return "MyNumber(%d)" % self.data
        # return "%d" % self.data
    
    def __add__(self, rhs):
        '''加号运算符的重载方法'''
        # print("__add__被调用")
        # v = self.data + other.data
        # obj = MyNumber(v)  # 创建一个新对象
        # return obj
        return MyNumber(self.data + rhs.data)
    def __sub__(self,rhs):
        # s = self.data - other.data
        # s1 = MyNumber(s)
        # return s1
        return MyNumber(self.data - rhs.data)
    
    # def __sub__(self, rhs):
    #     return MyNumber(self.data - rhs.data)

n1 = MyNumber(100)
n2 = MyNumber(200)
# n3 = n1.__add__(n2)  # MyNumber(300)
n3 = n1 + n2  # 等同于n1.__add__(n2)
print(n1, "+", n2, "=", n3)
n4 = n1 - n2
print(n1, "-", n2, "=", n4)



# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.money = 0
#         self.skill = []
#     def teach(self,other,skill):
#         print(self.name,"教",other.name,"学",skill)
#         other.skill.append(skill)
#     def work(self,money):
#         print(self.name,"上班赚了",money)
#         self.money += money
#     def borrw(self,other,money):
#         self.money += money
#         other.money -= money
#     def show_info(self):
#         print(self.age,"岁的",self.name,"有钱：",self.money,"他学会的技能是:",self.skill)



# zhang3 =Human("张三","35")
# li4 = Human("李四","8")
# zhang3.teach(li4,"Python")
# li4.teach(zhang3,"王者荣耀")
# zhang3.work(1000)
# li4.borrw(zhang3,200)
# zhang3.show_info()
# li4.show_info()