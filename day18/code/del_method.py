#此示例示意析构方法

# class Car:
#     def __init__(self,info):
#         self.info = info
#         print("汽车",info,"对象已建立")
#     def __del__(self):
#         print("汽车",self.info,"对象即将销毁")

# c1= Car("BYD E6")
# c2 = c1
# del c1
# input("请按回车继续")


class Dog:
    pass
dog1 = Dog()
print(dog1.__dict__)  # {}

dog1.kinds = "哈士奇"
dog1.color = "黑白"

print(dog1.__dict__)  # {'color': '黑白', 'kinds': '哈士奇'}