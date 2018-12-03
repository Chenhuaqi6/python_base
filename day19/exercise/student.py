class Student:
    infos = []
    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.score = s
    @classmethod
    def add_student(cls):
        n = input("姓名")
        a = int(input("年龄"))
        s = int(input("成绩"))
        cls.infos.append(Student(n,a,s))
    @classmethod
    def del_student(cls):
        n = input("请输入删除姓名:")
        for i , s in enumerate(cls.infos):
            if s.name == n:
                del cls.infos[i]
                print("删除成功")
                return
        print("删除失败")
Student.add_student()
Student.del_student()


