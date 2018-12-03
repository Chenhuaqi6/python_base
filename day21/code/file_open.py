# file_open.py
try:
    fr = open("myfile.txt","rt")
    try:
        s = fr.readline()
        print("第一行的长度是:",len(s))
        fr.close()
        int((input("请输入整数")))
    finally:
        fr.close()
except OSError:
    print("打开文件失败")