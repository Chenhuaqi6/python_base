#while.py

#用循环语句ｗｈｉｌｅ语句打印２０行ｈｅｌｌｏ

# 创建一个循环变量来控制循环次数
n = int(input("请输入一个整数: "))

i = 1
while i <= n:
    print("这是第%d行" % i)
    i += 1
else:
    print("while语句的else子句被执行")

