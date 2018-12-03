# numbers = [10086, 10000, 10010, 95588]
# names = ['中国移动', '中国电信', '中国联通']
# for t in zip(numbers, names):
#     print(t)
# for No, number, name in zip(range(1, 100),numbers,names):
#     print("序号",No, name, '的客服电话是:', number)


# names = ['中国移动', '中国电信', '中国联通']

# for t in enumerate(names,1):
#     print(t)  #(0, '中国移动')(1, '中国电信')(2, '中国联通')
# for t in enumerate(names, 101):
#     print(t)  #(101, '中国移动')(102, '中国电信')


# 练习:
#   写一个程序，读入任意行文字，当输入空行时结束输入
#   打印带有行号的输入结果
#     如:
#       请输入: abcde<回车>
#       请输入: hello<回车>
#       请输入: bye<回车>
#       请输入: <回车>
#     输出如下:
#       第1行: abcde
#       第2行: hello
#       第3行: bye

l=[]
while 1:
    n = input("请输入: ")
    if not n:
        break
    l.append(n)
for t in enumerate(l,1):
    print("第%d行:%s" % t)