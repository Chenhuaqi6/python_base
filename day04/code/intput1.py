#输入
# s = input("请输入你要去的城市： ")
# print("你要去的城市是： ", s)

# print(1, 2, 3, 4,sep="")
# print(1,2,3,4,end="\n\n\n")
# print(1,2,3,4,)

# x = int(input("请输入一个整数： "))
# y = int(input("再输入一个整数： "))
# z = x + y
# i = x*y
# o = x**y
# print("和为:%d,乘积：%d,次方:%d" % (z,i,o))


# h = int(input("输入小时: "))
# m = int(input("输入分钟: "))
# s = int(input("输入秒: "))
# l = h * 3600 + m * 60 + s
# print("一共过了：%d秒" % l)






my = int(input("输入您的社保基数: "))
yl = my * 0.08
gs = my * 0
yil = my * 0.02 + 3
zf = my * 0.12
zh = yl + gs + yil + zf 
gsyl = my * 0.19
gsgs = my * 0.05
gsyil = my * 0.1
gszf = my * 0.12
gszh = gsyl + gsgs + gsyil + gszf 
yg = gszh + zh 
print("您的养老保险为:%d,您的工伤保险为:%d,您的医疗保险:%d\
,您的住房公积金:%d,个人总缴费:%d" % (yl,gs,yil,zf,zh), end="\n\n")
print("公司需交养老保险:%d,公司需交工伤保险:%d,公司需交医疗保险:%d,公司需交住房公积金:%d,\
公司需交总金额:%d" % (gsyl,gsgs,gsyil,gszf,gszh))
print("国家拿到:%d" % (yg))
