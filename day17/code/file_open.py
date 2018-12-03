#file_open.py
# 文件的基本操作分为三步
try:
    #　１　打开
    # myf = open("myfile.txt") #相对路径
    # myf = open("我是不存在的文件.txt")
    print("文件打开成功")
    filename = "/home/tarena/nt_py/day17/code/myfile.txt"

    myf = open(filename)
    #２读／写文件
    line1 = myf.readline()
    print("此行长度是:%d,内容是:" % len(line1),line1)

    line2 = myf.readline()
    print("第二行：", line2)

    line3 = myf.readline()
    print("第三行：",line3)

    line4 = myf.readline()
    if line4 =="":
        print("已到末尾")



    # 3关闭文件
    myf.close()
    print("文件已经关闭")
except OSError:
    print("文件打开失败")