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
    l = myf.readlines()  #把文件内容形成字符串返回回来
    print(l)



    # 3关闭文件
    myf.close()
    print("文件已经关闭")
except OSError:
    print("文件打开失败")