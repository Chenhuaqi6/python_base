#此文件定义一个类　此类记录学生对象的行为及属性


class Student:
    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.score =s
    def get_student(self):
        """此方法返回当前对象自己的信息的元组"""
        return(self.name,self.age,self.score)