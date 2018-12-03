##练习
# 写一个程序，让用户分俩次输入一个人的信息：
# 　　信息包含：　姓名　和电话号码
# 让用户输入多个人的信息，当输入姓名为空时，结束输入
# 把用户输入的数据存于字典中
# 　姓名作为键，电话号码作用值
# 最后打印存储数据的字典
# 如：
# 请输入姓名：小张
# 请输入电话：
# 请输入姓名：
# 请输入电话
# 请输入姓名：《回车》
# 打印｛“小张”：１３８５５５５５，”小李“：４５６４６４６｝
# a = {}
# while True:
#     name = input("请输入姓名: ")
#     if name == "":
#         break
#     phone = int(input("请输入电话: "))
#     a[name]=phone
# print(a)


# book = dict() #book = {} 创建一个容器
# while True:
#     n = input("")
#     if not n:
#         break
#     a = int(input(""))
#     book[n]=a
# print(book)

# 写程序
# 　１、将seasons 写成字典
# 　　　键　　　　　　值
# 　１＝＝>         春季有１，２，３月


seasons = {}
seasons[1]="春季有1,2,3月"
seasons[2]="夏季季有4,5,6月"
seasons[3]="秋季有7,8,9月"
seasons[4]="冬季有10,11,12月"
print(seasons)

n = int(input("请输入一个整数: "))
if n <= 4:
    print(seasons[n])
else:
    print("cw")


# 练习：
# 　　输入一段字符串，打印出这个字符串中出现过的字符及出现的次数

# a = {}
# n = input("请输入一段字符串: ")
# for x in n:
#     if x not in a:
#         a[x] = 1
#     else:
#         a[x]+=1
# print(a)
# for k,v in a.items():
#     print("%s出现:%d次" % (k,v) )


###练习
# L = ["Tarena","xiaozhang","xiaowang"]
# a={x:len(x) for x in L}
# print(a)

# # 方法２：
# d = {}
# for s in L:
#     d[s] = len(s)
# print(d)

# Nos = [1001, 1002, 1005, 1006]
# names = ["Tom","Jerry","Spike","Syke"]
# d = {Nos[i]:names[i] for i in range(4) }
# print(d)

# d={}
# for i in range(4):
#     d={Nos[i]:names[i]}
#     print(d,end=" ")
# print()
