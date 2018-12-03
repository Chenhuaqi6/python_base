#slots.py
#此示例示意__slots__列表定义方法和用法

class Human:
    #此__solots__列表让Human创建的对象只允许有name age 属性
    __slots__ = ["name",'age']
    def __init__(self,n,a):
        self.name = n
        self.age = a
    def show_infos(self):
        print(self.name,"今年",self.age,"岁")
h1 = Human("Tarena",15)
h1.show_infos()
#此处会报错，因为此属性不在__slots__列表内
# h1.Age = 16
h1.show_infos()
h1.age = 18
h1.show_infos()

