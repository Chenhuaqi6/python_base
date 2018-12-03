#if _embed.py

mouth = int(input("请输入月份（1-12）: "))
if 1 <= mouth <= 12:
    print("输入正确")
    if mouth <=3:
        print("春季")
    elif mouth <= 6:
        print("夏季")
    elif mouth <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您的输入有误！！！")
