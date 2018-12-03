#binary_file_read.py


#此示例示意用二进制文件操作来读取文本文件里的内容


try:
    f = open("myfile.txt", "rb")
    b = f.read(5)
    print(b)
    print("字节串的长度为: ",len(b))
    b2 = f.read()
    print("字节串b2的长度是: ",len(b2))
    b3 = f.read()
    print(b3 == b"")
    f.close()
    s= b2.decode(encoding="utf-8")
    print(s)
except OSError:
    print("打开文件失败")