class Human:
    def __init__(self,n,a):
        print("human类的__init__被调用")
        self.name = n
        self.age = a
        # super().__init__() #显示调用object类的__init__方法
    def infos(self):
        print("姓名",self.name)
        print("年龄",self.age)

class Student(Human):
    def __init__(self,n,a,s = 0):
        super().__init__(n,a)
        self.score = s
    def show(self):
        super().infos()
        print("成绩",self.score)
    

s1 = Student("张奔",18,150)
s1.show()
h1 = Human("陈华齐",'21')  #此时会调用__init__方法
h1.infos()
