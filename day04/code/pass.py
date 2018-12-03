#pass.py


#让用户输入1~12的数字，如果不符合条件，则提示输入条件
n = int(input("请输入数字0-12: "))
if 0 <= n <= 12:
    pass#print("条件满足")
else:
    print("您输入有误！！！")