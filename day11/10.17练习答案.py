# def myadd(n):
#     i = 0
#     s = 0
#     while i <= n:
#         s += i
#         i += 1
#     return s
# number = int(input("请输入一个数: "))
# l = myadd(number)
# print(l)

# def myfac(n):
#     s = 1
#     for i in range(1,n+1):
#         s *= i
#     return s
# number = int(input("请输入一个数: "))
# print(myfac(number))

# def mymul(n):
#     s = 0
#     for i in range(1,n+1):
#         s += i**i
#     return s
# number = int(input("请输入一个数: "))
# print(mymul(number))

#录入学生信息
def input_student(l):
    # infors=[]
    while True:
        name = input("请输入姓名: ")
        if name == "":  #if not name:
            break
        age = int(input("请输入年龄: "))
        score = int(input("请输入成绩: "))
        D = {}
        D["姓名"] = name 
        D["年龄"] = age
        D["成绩"] = score
        l.append(D)
    return l
#输出学生信息
def output_student(infors):    
    print("+---------------+-----------+----------+")
    print("|     姓名      |    年龄   |   成绩   |")
    print("+---------------+-----------+----------+")
    for D in infors:
        #取值
        name = D["姓名"]
        age = D["年龄"]
        score = D["成绩"]
        age = str(age)
        score = str(score)
        #以列表方式打印出来
        print("|"+name.center(15)+"|"+age.center(11)+"|"+score.center(10)+"|")
        print("+---------------+-----------+----------+")
#删除学生全部信息
def rm(infos):
    s =input("请输入你要删除的姓名: ")
    for x in infors:
        if x["姓名"] == s:
            infors.remove(x)
#修改成绩
def change(infos):
    a = input("请输入您要修改学生的名字: ")
    k = input("请输入您要修改的成绩: ")
    for i in infors:
        if i["姓名"] == a:
            i["成绩"] = k
#菜单
def menu():
    print("+"+"-"*22+"+")
    print("|"+"1) 添加学生信息"+" "*7+"|")
    print("|"+"2) 查看学生信息"+" "*7+"|")
    print("|"+"3) 删除学生信息"+" "*7+"|")
    print("|"+"4) 修改学生信息"+" "*7+"|")
    print("|"+"5) 退出管理系统"+" "*7+"|")
    print("+"+"-"*22+"+")
infos = []
while True:
    menu()
    want = input("请输入您想要的操作: ")

    if want == "1":
        infors = input_student(infos)
        print(infors)
        print("添加成功")
    if not want:
        print("请重新输入: ")
        
    if want == "2":
        output_student(infos)
    if want == "3":
        rm(infors)
    if want == "4":
        change(infors)
    if want == "q":
        print("感谢使用")
        break



