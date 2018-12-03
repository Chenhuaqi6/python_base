def myadd():
    L =[]
    while 1:
        n = input("请输入姓名: ")
        if not n:
            break
        a = int(input("请输入年龄: "))
        s = input("请输入地址: ")
        L.append(dict(name= n,age= a,address= s))
    return L

def save_infos(L,filename="infos.txt"):

    try:
        f = open(filename,"w")
        try:
            for d in L:
                f.write(d["name"])
                f.write(",")
                f.write(str(d["age"]))
                f.write(",")
                f.write(d["address"])
                f.write("\n")
        finally:
            f.close()
    except OSError:
        print("打开文件失败")
def print_info(a):
    for d in a:
        print(d["name"],"今年",d["age"],"岁 成绩是：",d["address"])

L = myadd()
print(L)
save_infos(L)
print_info(L)
