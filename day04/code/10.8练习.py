# # 　１．北京出租车计价器：
# # 　　　收费标准：
# # 　　　　　　３公里以内收费　１３元
# # 　　　　　　基本单价　２．３元／公里（超出３公里以外）
# # 　　　　　　空驶费：超过１５公里后，每公里加收单价的５０％的空驶费（３．４５／公里）
# # 　　　　　　要求：
# # 　　　　　　　　输入公里数，打印出费用金额

# km = float(input("请输入公里数: "))
# if km <= 3:
#     money = 13
#     print("需要支付: ",round(money),"元")
# elif 3 < km <= 15:
#     money = (km-3) * 2.3 + 13
#     print("需要支付: ",round(money),"元")
# elif km > 15:
#     money = (km-3) * 2.3 + 13 + 3.45 * (km - 15) 
#     print("需要支付: ",round(money),"元")

# # ２、输入一个学生的三科成绩
# # 　　　　１、打印出最高分是多少分？
# # 　　　　２、打印出最低分是多少分？
# # 　　　　３、打印出平均分是多少分？

# # s = int(input("数学成绩为: "))
# # l = int(input("语文成绩为: "))
# # q = int(input("英语成绩为: "))
# # max = l 
# # if s > l:
# #     max = s
# # if q > l:
# #     max = q 
# # print("最大值是",max)
# # min = s
# # if s > l:
# #     min = l
# # if l > q:
# #     min = q
# # print("最小值是：",min)
# # p = (s+l+q)/3
# # print("平均成绩为:%.2f" % (p))

# # ３、计算　ＢＭＩ指数（Body Mass Index） 又称身体质量指数
# # 　计算公式：
# # 　　ＢＭＩ　＝　体重（公斤）／身高的平方（米）
# # 如：一个６９公斤的人，身高１７３公分，则　６９／１．７３＊＊２　＃　得２３．０５
# # 　标准表：
# # 　　　ＢＭＩ<18.5 体重过轻
# # 　　　　１８．５< BMI <24 体重正常
# # 　　　ＢＭＩ　>= 24 体重过重
# # 　　要求：输入身高和体重，并打印出ＢＭＩ的值，并打印体重状况

# w = float(input("请输入您的体重（公斤）: "))
# h = float(input("请输入您的身高（米）: "))
# BMI = w / h**2
# if BMI < 18.5:
#     print("您的BMI指数为: ",round(BMI,2),"您的体重过轻")
# elif 18.5 < BMI < 24:
#     print("您的BMI指数为%.2f，您的体重正常" % BMI)
# else:
#     print("您的身高是{1}米，您的体重是{2}公斤，您的BMI指数为{0:.2f}您的体重过重".format(BMI,h,w))



l = int(input("请输入宽度: "))
w = "#" * l
print(w)
line = "#" + " " * (l - 2) + "#"
print(line)
print(line)
print(w)
