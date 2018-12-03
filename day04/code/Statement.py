#此示例语句

# print("hello world")
# x = 100 + 200
# print(x)

# h = int(input('请输入小时: '))
# m = int(input('请输入分钟: '))
# s = int(input('请输入秒: '))
# second = h * 3600 + m * 60 + s
# print('距离０：０：０过了',second,'秒')

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
print("您的养老保险为:%d\n您的工伤保险为:%d\n您的医疗保险:%d\
\n您的住房公积金:%d\n个人总缴费:%d\n" % (yl,gs,yil,zf,zh), end="\n")
print("公司需交养老保险:%d\n公司需交工伤保险:%d\n公司需交医疗保险:\
%d\n公司需交住房公积金:%d\n公司需交总金额:%d" % (gsyl,gsgs,gsyil,gszf,gszh))
print("国家拿到:%d" % (yg))