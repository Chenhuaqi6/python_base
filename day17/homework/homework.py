def mycopy(use_filename,get_filename):
    try:
        f1=open(use_filename,"rb")
        try:
            try:
                f2 = open(get_filename,"wb")
                while 1:
                    s = f1.read(2)
                    
                    if not s:
                        break
                    b = f2.write(s)
                    
            except OSError:
                print("打开目标文件失败")
        finally:
            f1.close()
    except OSError:
        print("打开源文件失败")

use = input("请输入源文件: ")
get = input("请输入目标文件: ")

mycopy(use,get)