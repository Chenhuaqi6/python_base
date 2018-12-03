from student_info import input_student
L=[]
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
def print_info(a):
    for d in a:
        print(d["姓名"],"今年",d["年龄"],"岁 成绩是：",d["成绩"])

IT = input_student(L)
print(IT)
save_infos(IT)
print_info(IT)
