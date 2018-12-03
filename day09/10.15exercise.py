# def sum3(a,b,c):
#     s = a+b+c
#     return s
# # print(sum3(pow3(1),pow3(2),pow3(3)))
# def pow3(x):
#     i = x**3
#     return i
# print("和为: ",sum3(pow3(1),pow3(2),pow3(3)))
# print("立方为: ",pow3(sum3(1,2,3)))


def input_student():
    infors = []
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
        infors.append(D)
    return infors
# print(input_student())

def output_student(infors):
    print("+---------------+-----------+----------+")
    print("|     姓名      |    年龄   |   成绩   |")
    print("+---------------+-----------+----------+")
    for D in infors:
        name = D["姓名"]
        age = D["年龄"]
        score = D["成绩"]
        age = str(age)
        score = str(score)
        print("|"+name.center(15)+"|"+age.center(11)+"|"+score.center(10)+"|")
        print("+---------------+-----------+----------+")

infos = input_student()
print(infos)
output_student(infos)

# def Sn(n):
#     s = 0
#     # n = int(input("请输入"))
#     for x in range(1,n+1):
#         k = x+1
#         s += 1/(x*k)
#     return s
# print(Sn(3))
# print(Sn(1000)) 