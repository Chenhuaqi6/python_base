infos = []  # 创建一个列表容器准备存放每个学生信息的字典
while True:
    n = input("请输入姓名: ")
    if not n:  # 如果姓名为空,则结束输入
        break
    a = int(input("请输入年龄: "))
    s = int(input("请输入成绩: "))
    # 新创建一个字典 {}  dict()
    d = {'name':n, 'age':a, 'score':s}  # d = dict(name=n, age=a, score=s)
    infos.append(d)

# 打印存有学生信息的字典的列表
print(infos)

print("+---------------+-----------+----------+")
print("|     姓名      |    年龄   |   成绩   |")
print("+---------------+-----------+----------+")
for d in infos:  # d绑定字典
    n = d['name']
    a = d['age']
    s = d['score']
    a = str(a)  # 将整数转为字符串
    s = str(s)
    print("|" + n.center(15) + '|'+ a.center(11) + '|'+ s.center(10) + '|')

# print("|    tarena     |     15    |    99    |")
# print("|     china     |     70    |    98    |")
print("+---------------+-----------+----------+")
