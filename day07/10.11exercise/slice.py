# 练习：
# 　　已经有列表
# 　　　　L = [3,5]
#   用索引和切片操作，将原列表改变为：
#   　　L = [1,2,3,4,5,6]
#   将列表反转
#   　L = [6,5,4,3,2,1]
#   然后删除最后一个元素
#   　L = [6,5,4,3,2]
# L = [3,5]
# L += [6]
# L[1:1] = [4]
# L[0:0] = [1,2]
# print("L=", L)
# L[::-1] =L
# print("L=", L)
# print("L=", L)



# L = []
# while True:
#     s = int(input("请输入整数：　"))
#     if s < 0:
#         break
#     L += [s]
# print(L)
# n = 0
# count = 0
# for i in L:
#     n +=i
#     count += 1
#     #P = n/(len(L))
#     if i > s:
#         max = i

# print("平均数是:%.2f" % (n / count))
# print("最大值为", max)

# 求最大
# 先假设第一个最大
# max = L[0]
# i = 1
# while i < count:
#     x = L[i]
#     if x > max:
#         max = x
#     i += 1
# print(最大”，ｍａｘ



# 练习：
# 　小于０时结束输入
# 　１、最大的数
# 　　２、第二大的数
#   把最大的全删除了

# 　　　３、删除最小的

L = []
while True:
    s = int(input("请输入正整数: "))
    if s < 0:
        break
    L += [s]  #L.append(s)
print("最大的数:%d,最小的：%d " % (max(L),min(L)))
L2 = L.copy() #复制一份
zuida =  max(L2)
while zuida in L2:
    L2.remove(zuida)
dierda = max(L2)
print("第二大的为: ",dierda)
zuixiao = min(L)
L.remove(zuixiao)
print("最后的列表为: ",L)



