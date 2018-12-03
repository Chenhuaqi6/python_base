###homework

# 函数名 	描述
# R.random() 	返回一个[0, 1) 之间的随机实数
# R.uniform(a,b) 	返回[a,b] 区间内的随机实数
# R.randin(a, b) 	返回在[a, b]范围内的整数(包含a,b)
# R.randrange([start,] stop[, step]) 	返回range(start,stop,step)中的随机数
# R.choice(seq) 	从序列中返回随意元素
# R.shuffle(seq[, random]) 	随机指定序列的顺序(乱序序列）
# R.sample(seq,n) 	从序列中选择n个随机且不重复的元素




# import random
# a = "\u2660"
# b = "\u2663"
# c = "\u2666"
# d = "\u2665"
# l = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# L1 = []
# L2 = []
# L3 = []
# L4 = []
# for x in l:
#     #收集各个花色的所有牌
#     L1.append(a+x)
#     L2.append(b+x)
#     L3.append(c+x)
#     L4.append(d+x)
# e = L1+L2+L3+L4     #所有牌放到一个列表中
# e.append("小王")
# e.append("大王")        #＝添加大王，小王

# one = random.sample(e,17)
# e=set(e)-set(one)
# two = random.sample(e,17)
# e = set(e)-set(two)
# three = random.sample(e,17)     #随机出３组　每组１７张
# e = set(e)-set(three)

# begin1 = input("输入回车发牌: ")
# if begin1 == "":
#     print("第一个人的牌: ",one)
# begin2 = input("输入回车发牌: ")
# if begin2 == "":
#     print("第二个人的牌: ",two)
# begin3 = input("输入回车发牌: ")
# if begin3 == "":
#     print("第三个人的牌: ",three)
# begin4 = input("输入回车发牌: ")
# if begin4 == "":
#     print("底牌为: ",e)


# 打印杨辉三角


def get_next_line(L):
    '''L代表当前一行
    返回当前行的下一行
    如: L = [1, 2, 1]

    返回   [1, 3, 3, 1]
    '''
    # 最左侧加一个1
    rl = [1]  # 准备要返回的列表
    # 中间 加 len(L)-1个数
    for i in range(len(L)-1):
        rl.append(L[i] + L[i + 1])
    # 最右侧加一个1
    rl.append(1)
    return rl

def get_yanhui_list(n):  # n代表行数
    '''返回: [
        [1],
        [1, 1],
        [1, 2, 1],
        ...
    ]'''
    rl = []  # 此列表用于返回
    line = [1]  # 当前要处理的一行
    for _ in range(n):
        rl.append(line)  # 把当前行放进去
        line = get_next_line(line)
    return rl

def get_yanghui_string(L):
    ''' 如果L = [[1], [1, 1], [1, 2, 1]]
    返回rl = ["1", "1 1", "1 2 1"]
    '''
    rl = []
    for line in L:
        # 把 line=[1, 2, 1] 转为line=['1', '2', '1']
        line = [str(x) for x in line]
        s = ' '.join(line)
        rl.append(s)
    return rl

def print_yanghui_triangle(n):
    # 打印n行的杨辉三解
    L = get_yanhui_list(n)
    SL = get_yanghui_string(L)  # 字符串列表
    # 求最大长度:
    max_len = len(SL[-1])
    for line in SL:
        print(line.center(max_len))


print_yanghui_triangle(10)


# 测试函数
# L = get_yanhui_list(6)
# print(get_yanghui_string(L))
# # print(get_next_line([1]))

l=[1]
row=int(input("请输入"))
width = row*4 #宽度


def 