 #示意Ｆ．write 和F.writelines 方法进行文件写操作

try:
    f = open("mynote.txt","w") #以写方式打开

    f.write("ABC中文")
    f.writelines(["123","abc","结束"])
    f.write("!")

    f.close()
except OSError:
    print("打开文件失败")