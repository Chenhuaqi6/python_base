#init_method.py

#此示例示意初始化方法的定义方法及用法

# class car:
#     def __init__(self,n,a,b):
#         self.name = n   #名字
#         self.color = a  #颜色
#         self.brand = b  #型号

#     def run(self,speed):
#         print(self.color,"的",self.name,self.brand,"正在以",speed,"速度行驶")

# s1 = car("宝马","白色","x5")
# s2 = car("雷克萨斯","灰色","e250")
# s1.run(180)
# s2.run(250)



# class Studen:
#     def __init__(self,name,age,score=0):
#         self.name=name
#         self.age=age
#         self.score = score

#     def set_score(self,score):
#         self.score = score
#     def show_info(self):
#         print(self.name,"今年",self.age,"成绩为: ",self.score)
# L = []
# L.append(Studen("小张",20,100))
# L.append(Studen("小z",21,99))
# L.append(Studen("小w",20,85))
# L[-1].set_score(70)
# for s in L:
#     s.show_info()

# class human:
#     def __init__(self,name1,name2,age1,age2):
#         self.name1 = name1
#         self.name2 = name2
#         self.age1 = age1
#         self.age2 = age2
    
#     def teach(self,what):
#         print(self.name1,"教",self.name2,"学",what)
#     def 

# s1 = human("张三","李四","35","8")
# s1.teach("python")
class human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.money = 0
        self.skill = []
    #一个类　定义对象　每个对象一一对应　干什么事情　得到什么　失去什么　都必须考虑　
    def teach(self,other,skill):
        other.skill.append(skill)
        print(self.name,"教",other.name,"学",skill)

    #谁上班　谁的钱加
    def work(self,money):
        self.money += money
        print(self.name,"上班赚了",money)

    #谁向谁借　谁得到　谁失去
    def borrow(self,other,money):
        if other.money >= money:
            self.money+=money
            other.money -= money
        print(self.name,"向",other.name,"借了",money)

    #打印一个人的全部信息
    def show_info(self):
        print(self.age,"岁的",self.name,"有钱",self.money,"他学会的技能是:",self.skill)

zhang3 = human("张三",35)
li4 = human("李四",8)
zhang3.teach(li4,"python")
li4.teach(zhang3,"王者荣耀")
zhang3.work(100)
li4.borrow(zhang3,2)
zhang3.show_info()
li4.show_info()