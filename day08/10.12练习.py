# for i in range(1,10):
#     for k in range(1,i+1):
#         print("{0}x{1}={2}".format(i,k,i*k),end=" ")
#     print()


# x,y=0,1
# while y <=40:
#     print(y,end=" ")
#     x,y=y,x+y
# print()

# l = [1,1]
# for i in range(38):
#     l.append(l[i]+l[i+1])
# print(l)

# a = 1
# for i in range(1,10):
#     a = (a+1) * 2
# print("一共%d个桃子" % a)


infors = []
while True:
    name = input("请输入姓名: ")
    if name == "":  #if not name:
        break
    age = int(input("请输入年龄: "))
    score = int(input("请输入成绩: "))
    D = {}
    D["姓名"] = name 
    D["年龄"] = age
    D["成绩"] = score
    infors.append(D)
print(infors)
print("+---------------+-----------+----------+")
print("|     姓名      |    年龄   |   成绩   |")
print("+---------------+-----------+----------+")
for x in infors:
    n = x["姓名"]
    a = x["年龄"]
    s = x["成绩"]
    a = str(a)
    s = str(s)
    print("|"+n.center(15)+"|"+a.center(11)+"|"+s.center(10)+"|")
    print("+---------------+-----------+----------+")


# print(infos)

# print("+---------------+-----------+----------+")
# print("|     姓名      |    年龄   |   成绩   |")
# print("+---------------+-----------+----------+")
# for d in infos:  # d绑定字典
#     n = d['name']
#     a = d['age']
#     s = d['score']
#     a = str(a)  # 将整数转为字符串
#     s = str(s)
#     print("|" + n.center(15) + '|'
#               + a.center(11) + '|'
#               + s.center(10) + '|')

# # print("|    tarena     |     15    |    99    |")
# # print("|     china     |     70    |    98    |")
# print("+---------------+-----------+----------+")

