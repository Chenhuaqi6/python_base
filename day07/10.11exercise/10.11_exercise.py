# #练习
# １、有一些数字存在于列表中，如：
# L = [1,3,2,16,4,2....,98,82]
# 1)将列表中出现的数字存入到另一个列表L2中
# 　　要求：重复出现多次的数字只能在Ｌ２中保留一份（去重）
# ２）将列表中出现俩次的数字存于Ｌ３列表中只保留一份、

# ２、生成一个列表，求ｘ的平方＋１的列表，跳过结果能被５整除的数（０<=x<=100）

# 3、把０－１００之间的所有素数存于一个列表中

# L = [1,1,2,2,3,3,4,4,5,5,6,]
# L2 = []  #用于存放不重复的数
# for a in L:
#     #如果a 在Ｌ２中不存在，将ａ放入Ｌ２
#     if a not in L2:
#         L2.append(a)
    
# print("去重后:L2= ",L2)

# L = [1,1,2,2,3,3,3,4,4,5,5,6,6]
# L3 = []
# for x in L:
#     if x not in L3 and L.count(x) == 2:
#         L3.append(x)
# print(L3)
        
# L = [x**2+1 for x in range(0,101) if (x**2+1 % 5) != 0] 
# print(L)

# L = []
# for x in range(0, 101):
#     if (x**2 % 5) != 0:
#         L.append(x**2+1)
# print(L)

L = []
for x in range(101):
    if x < 2: #不是素数
        continue    #回到循环
        #走到此　一定都大于２
    for y in range(2,x):    #判断ｘ能否被２，３，４，５，６，７到ｘ之前的数
        if x % y ==0:
            # x 一定不是素数
            break
    else:   #走到这ｘ一定是素数
        L.append(x)
print(L)

    