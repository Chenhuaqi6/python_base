# def names(n):
#     if n == 1:
#         return 10
#     return names(n-1)+2
# print("第二位年龄为",names(2))
# print("第三位年龄为",names(4))
# print("第四位年龄为",names(4))
# print("第五位年龄为",names(5))


# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def print_list(lst):
#     for x in lst:
#         if type(x) is list:
#             print_list(x)
#         else:
#             print(x,end=" ")
# print_list(L)

# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def sum_list(lst):
#     s = 0
#     for x in lst:
#         if type(x) is list:
#            s += sum_list(x)
#         else:
#             s += x
#     return s
# print(sum_list(L))

#录入学生信息
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
    for x in infors:
        if x["姓名"] == s:
            infors.remove(x)

#修改成绩
def change(l):
    a = input("请输入您要修改学生的名字: ")
    k = input("请输入您要修改的成绩: ")
    for i in l:
        if i["姓名"] == a:
            i["成绩"] = k
#菜单
def menu():
    print("+"+"-"*31+"+")
    print("|"+"1) 添加学生信息"+" "*16+"|")
    print("|"+"2) 查看学生信息"+" "*16+"|")
    print("|"+"3) 删除学生信息"+" "*16+"|")
    print("|"+"4) 修改学生信息"+" "*16+"|")
    print("|"+"5) 按学生成绩高－低显示学生信息"+"|")
    print("|"+"6) 按学生成绩低－高显示学生信息"+"|")
    print("|"+"7) 按学生年龄高－低显示学生信息"+"|")
    print("|"+"8) 按学生年龄低－高显示学生信息"+"|")
    print("|"+"q) 退出管理系统"+" "*16+"|")
    print("+"+"-"*31+"+")
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
#主函数

def main():
    infos = []
    while True:
        
        menu()
        want = input("请输入您想要的操作: ")

        if want == "1":
            print(input_student(infos))
            print("添加成功")
        if not want:
            print("请重新输入: ")
            
        if want == "2":
            output_student(infos)
        if want == "3":
            rm(infos)
        if want == "4":
            change(infos)
        if want == "5":
            highg_d(infos)
        if want == "6":
            lowd_g(infos)
        if want == "7":
            h_d(infos)
        if want == "8":
            d_h(infos)
        if want == "q":
            print("感谢使用")
            break
main()