try:
    f = open("phone.txt","w")
    while 1:
        n =input("请输入姓名:")
        p =input("请输入电话:")
        f.writelines(n)
        f.writelines(p)
        if not n:
            f.close()
            break
        
except OSError:
    print("打开文件失败")
