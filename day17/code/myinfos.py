
# try:
#     filename="/home/tarena/nt_py/day17/code/info.txt"
#     myf = open(filename)

#     while 1:
#         line =myf.readline()
#         if line == "":
#             break
#         line = line.strip()
#         l = line.split(",")
#         # name,age,score = l
#         print(l[0],"今年",l[1],"岁,成绩:",l[2])
#     myf.close()

# except OSError:
#     print("打开文件失败")

def read_info_from_file(filename = "info.txt"):
    l=[]
    try:
        file = open(filename)
        while 1:
            s = file.readline()
            if not s:
                break
            s.strip()
            lst = s.split(",")
            name,age,score = lst
            age = int(age)
            score = int(score)
            l.append(dict(name=name,age=age,score=score))
        file.close()
    except OSError:
        print("打开文件失败")
    return l

def print_info(a):
    for d in a:
        print(d["name"],"今年",d["age"],"岁 成绩是：",d["score"])
l = read_info_from_file()
print_info(l)