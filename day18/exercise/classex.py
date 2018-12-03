# class Human:
#     def set_info(self,name,age,address="不详"):
#         # print(name,"今年",age,"岁，家住:",address)
#         self.n = name
#         self.a = age
#         self.ad =address

#     def show_info(self):
#         print(self.n,"今年",self.a,"岁，家住",self.ad)



# s1 = Human()
# s1.set_info("小张",20,"深圳市南山区")
# s2 = Human()
# s2.set_info("小李",18)

# s1.show_info()
# s2.show_info()


class Human:
    def __init__(self,n,a,d):
        self.name = n
        self.age = a
        self.address = d
        
    def show_info(self):
        print(self.name,self.age,self.address)
s1 = Human("asd",20,30)
s1.show_info()

