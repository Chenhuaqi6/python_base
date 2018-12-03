#class_variable.py

# 示意类变量的定义，访问及赋值操作

# class Human:
#     total_count = 0     #创建一个类变量

# print("Human.total_count=",Human.total_count)
# Human.total_count += 100
# print(Human.total_count)

# Human.class_var2 = 200  #创建第二个类变量
# print(Human.class_var2)



# class Human:
#     total_count = 0 


# h1 = Human() #创建一个实例
# print(h1.total_count)   #0　＃访问类变量

# #类变量可以通过类的实例直接访问（取值）
# h1.total_count = 100   #此条语句是创建实例变量
# print(h1.total_count)
# print(Human.total_count)　　# 0  实例对像赋值　不与类变量相关


class Human:
    total_count = 0
h1 = Human()
h1.total_count +=100
print(Human.total_count)
h1.__class__.total_count = 200
print(Human.total_count)


# class Human:
#     total_count = 0
#     def __init__(self):
#         self.__class__.total_count +=1
#     def __del__(self):
#         self.__class__.total_count -=1
# h1 = Human()
# l = []
# l.append(Human())
# l.append(Human())
# print(Human.total_count)
# del h1
# del l
# print(Human.total_count)


