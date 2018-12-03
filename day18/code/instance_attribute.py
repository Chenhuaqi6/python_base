
#此示例示意实例属性的创建及使用
class Dog:
    def eat(self,food):
        print(self.color,"的",self.kinds,"正在吃",food)

        #在吃的过程中添加一个last_food属性用来记录此次吃的是什么
        self.last_food = food
    def show_info(self):
        print(self.color,"的",self.kinds,"上次吃的是",self.last_food)
    

dog1=Dog()

dog1.color = "黄色"
dog1.kinds = "京巴"

dog1.eat("骨头")


dog2 = Dog()
dog2.color = "白色"
dog2.kinds = "哈士奇"
dog2.eat("便便")

#打印每个小狗的信息
dog1.show_info()
dog2.show_info()

