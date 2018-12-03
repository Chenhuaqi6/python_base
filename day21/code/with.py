# try:
    # fr = open("myfile.txt","rt")
#     with open("myfile.txt","rt") as fr:
#         s = fr.readline()
#         print("第一行的长度是:",len(s))
#         int((input("请输入整数")))
# except OSError:
#     print("打开文件失败")
# except ValueError:
#     print('输入错误')


# with 打开之后不用输入关闭

# 3. 写程序，实现复制文件功能
#   要求:
#     1) 要考虑关闭文件问题
#     2) 要考虑超大文件复制问题
    # 3) 要能复制二进制文件(如:/usr/bin/python3 等文件)

def mycopy(src_filename, dst_filename):  # 源文件名和目标文件名
    try:
        with open(src_filename,"rb") as fr,open(dst_filename,"wb") as fw:

            while True:
                b = fr.read(4096)
                if not b:
                    break
                fw.write(b)

    except OSError:
        print("打开源文件失败")




src = input("请输入源文件名:")
dst = input("请输入目标文件名:")
mycopy(src, dst)