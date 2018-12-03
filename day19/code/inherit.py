#此示例示意单继承的用法

class Human:
    def say(self,what):
        print("say",what)
    def walk(self,distance):
        print("走了",distance,"公里")
    def play(self,what):
        print("玩了",what)
class Student(Human):
    def study(self,subject):
        print("学了",subject)
class Teacher(Student):
    def teach(sefl,what):
        print("教了",what)



h1 = Human()
h1.say("天气冷了")
h1.walk(5)

h2 = Student()
h2.say("有点累")
h2.walk(8)
h2.play("王者")
h2.study("python")

h3 = Teacher()
h3.study("opp")
h3.walk(10)
h3.say("同学们好")