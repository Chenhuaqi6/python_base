
try:

    print("文件打开成功")
    filename = "/home/tarena/nt_py/day17/code/myfile.txt"

    myf = open(filename)
    l = myf.readlines()  #把文件内容形成字符串返回回来
    print(l)


    myf.close()
    print("文件已经关闭")
except OSError:
    print("文件打开失败")



try:

    print("文件打开成功")
    filename = "/home/tarena/nt_py/day17/code/myfile.txt"

    s1  = myf.read()
    print(s1)
    print("s1的字符串表达式", repr(s1))
    s2 = myf.read(5)
    print(s2)
    s3 =myf.read(2)
    print(s3)
    s4 = myf.read()
    print(s4)



    
    myf.close()
    print("文件已经关闭")
except OSError:
    print("文件打开失败")


# ＃＃＃＃＃写文件+++++++++++++++

"w" "x" "a"

