#输入学生信息
def input_student(l):
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
def output_student(l):   
    print("输出",l) 
    print("+---------------+-----------+----------+")
    print("|     姓名      |    年龄   |   成绩   |")
    print("+---------------+-----------+----------+")
    for D in l:
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
def rm(l):
    s =input("请输入你要删除的姓名: ")
    for x in l:
        if x["姓名"] == s:
            l.remove(x)
#修改成绩
def change(l):
    a = input("请输入您要修改学生的名字: ")
    k = input("请输入您要修改的成绩: ")
    for i in l:
        if i["姓名"] == a:
            i["成绩"] = k
#按成绩从高到低排序
def highg_d(l):
    print(l)
    def high(i):
        return i["成绩"]
    a = sorted(l, key =high,reverse=True)
    # a = sorted(l,key= lambda d:d["成绩"])
    print("排序",a)
    output_student(a)
#按成绩从低到高
def lowd_g(l):
    def low(i):
        return i["成绩"]
    a = sorted(l,key=low)
    output_student(a)
#按年龄从高到底
def h_d(l):
    def ageg_d(i):
        return i["年龄"]
    a=sorted(l,key=ageg_d,reverse=True)
    output_student(a)
#按年龄从低到高
def d_h(l):
    def ageg_d1(i):
        return i["年龄"]
    a =sorted(l,key=ageg_d1)
    output_student(a)
#读取文件
def read_file(filename = "sis.txt"):
    try:
        f = open(filename,"r")
        try:
            s = f.read()
            print(s)
        finally:
            f.close()
    except OSError:
        print("打开文件失败")           
#保存信息
def save_infos(L,filename="sis.txt"):

    try:
        f = open(filename,"w")
        try:
            for d in L:
                f.write(d["姓名"])
                f.write(",")
                f.write(str(d["年龄"]))
                f.write(",")
                f.write(str(d["成绩"]))
                f.write("\n")
        finally:
            f.close()
    except OSError:
        print("打开文件失败")