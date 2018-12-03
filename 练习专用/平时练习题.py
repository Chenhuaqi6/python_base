# # D={}
# # D["TOM"]="python"
# # D["JEN"]="C"
# # D["JARY"]="PHP"
# # print(D)
# # friends = ["TOM","JARY"]
# # for Name in D.keys():
# #     print(Name)
# #     if Name in friends:
# #        print("hi"+Name) 

# def isprime(x):
#     if x < 2:
#         return False
#     # 此处x一定大于等于2
#     for i in range(2, x):
#         if x % i == 0:  # 整除就一定不是素数
#             return False
#     return True  # 走到此处x一定为素数

# print(isprime(3))  # True
# print(isprime(4))  # False

# def prime_m2n(m, n):
#     L = []
#     for x in range(m, n):
#         # 如果x是素数,把x放到列表中
#         if isprime(x):
#             L.append(x)
#     return L
# l = prime_m2n(10,20)
# print(l)
# def primes(n):
#     return prime_m2n(0, n)
# L = primes(10)
# print(L)  # [2, 3, 5, 7]

# d=[{"姓名":"chen","年龄":21,"成绩":100},{"姓名":"hua","年龄":22,"成绩":110}]
# for x in d:
#     a=x["姓名"]
#     b= x["年龄"]
#     c = x["成绩"]
#     print(a,b,c)
#     # d1=sorted(d,key=d["成绩"])

# def myage(n):
#     if n == 1:
#         return 10
#     s = myage(n-1)+2
#     return s
# print(myage(5))

# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def myfun(x):
#     for i in x:
#         if type(i) is list:
#             myfun(i)
#         else:
#             print(i,end=" ")
# myfun(L)
# print()

# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def myfun1(x):
#     s = 0
#     for i in x:
#         if type(i) is list:
#             s += myfun1(i)
#         else:
#             s += i
#     return s
# print(myfun1(L))


# def mysum(n):
#     s = 0
#     for i in range(1,n+1):
#         s += i
#     return s
# print(mysum(100))

# def myfac(n):
#     s = 1
#     for i in range(1,n+1):
#         s*=i
#     return s
# print(myfac(5))

# L = [{'姓名': 'ASDA', '成绩': 100, '年龄': 21}, {'姓名': 'ASDA', '成绩': 11, '年龄': 21}]
# for i in L:
#     n = i["姓名"]
#     a = i["年龄"]
#     s = i["成绩"]
#     print(n,a,s)


# l = [1,1]
# for x in range(38):
#     l.append(l[x]+l[x+1])
# print(l)

# s = 1
# for x in range(1,10):
#     s = (s+1)*2
# print(s)

# for x in range(1,10):
#     for y in range(1,x+1):
#         print("%dx%d=%d" % (x,y,x*y),end =" ")
#     print()

# l=[]
# while True:
#     n =input("请输入姓名: ")
#     if not n:
#         break
#     a =input("请输入年龄: ")
#     s =input("请输入成绩: ")
#     d={}
#     d["name"] = n
#     d["age"] = a
#     d["score"] = s
#     l.append(d)

# print(l)

# l=[1,2,3,4]
# s=[str(x) for x in l]
# print(s)
# q="-".join(s)
# print(q)

# s = "chenhuaqi"
# # q=s.split(" ")
# # print(q)
# # k = "#".join(q)
# # print(k)
# k = " ".join(s)
# s = k.split()
# print(k)
# print(s)

# s = [1,2,3,4,5,6,7,8,9,10]
# q = [str(x) for x in s]
# print(q)
# h = "x".join(q)
# print(h)



# l=[1,3,5,7]
# it = iter(l)
# try:
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration:
#     print("出现错误，已处理")

# def myevent(start,stop):
#     if start % 2 == 1:
#         start +=1
#     for i in range(start,stop,2):
#         yield i
# for x in myevent(11,20):
#     print(x,end=" ")

# def myfun(a,b):
#     if a % 2 == 1: #判断a的值　如果为奇数则　加上１
#         a+=1
#     for x in range(a,b,2):　
#         yield x
# for x in myfun(13,25):
#     print(x,end=" ")


# def myfun(n):
#     s = 1
#     for x in range(1,n+1):
#         s*=x
#         yield s
# l = list(myfun(5))
# print(l)
# print(sum(myfun(5)))

# gen = (x**2 for x in range(1,5))
# it =iter(gen)
# try:
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration:
#     print("出现错误，已处理")

# l = [2,3,5,7]
# def myfun(a):
#     for x in a:
#         s = x**2+1
#         yield s
# for x in myfun(l):
#     print(x)

# for y in (x**2+1 for x in l):
#     print(y)


# def myfun(a):
#     for x in a:
#         yield x
# s = [x**2+1 for x in myfun(l)]
# print(s)

# numbers = [10086, 10000, 10010, 95588]
# names = ['中国移动', '中国电信', '中国联通']

# for t in zip(numbers,names):
#     print(t)
# for t in zip(range(1,100),numbers,names):
#     print(t)
# for t in enumerate(names):
#     print(t)
# for t in enumerate(names,1): #数字在后面　没有的话默认从０开始

# l=[]
# while 1:
#     n = input("请输入: ")
#     if not n:
#         break
#     l.append(n)
# for t in enumerate(l,1):
#     print(t)

# def myfun(a,b):
#     for x in range(a,b):
#         if x < 2:

#             continue
#         for y in range(2,x):
#             if x % y == 0:
#                 break
#         else:
#             yield x
# my = [x for x in myfun(0,20)]
# print(my)

# def myrange(*args):
#     if len(args) == 1:
#         i = 0
#         while i<args[0]:
#             yield i
#             i += 1
#     if len(args) == 2:
#         i =args[0]
#         while i < args[1]:
#             yield i
#             i += 1
#     if len(args) == 3 and args[2] >0:
#         i = args[0]
#         while i < args[1]:
#             yield i
#             i += 1+args[2]
#     if len(args) == 3 and args[2] < 0:
#         i = args[0]
#         while i > args[1]:
#             yield i
#             i += args[2]
# my = [x for x in myrange(10,2,-1)]
# print(my)


# def myfun(n):
#     a =1
#     b = 0
#     for _ in range(n):
#         a,b=b,a+b
#         yield b
# my = [x for x in myfun(40)]
# print(my)
# print(sum(my))

# s = {"唐生","悟空","八戒","沙僧"}
# my = iter(s)
# while 1:
#     try:
#         print(next(my))
#         print(next(my))
#         print(next(my))
#         print(next(my))
#         print(next(my))
#         print(next(my))
#         print(next(my))
#         print(next(my))
#         print(next(my))
        
#     except StopIteration:
#         print("遍历结束")
#         break


# def get_last_high(hight,times):
#     for _ in range(times):
#         hight /= 2
#     return hight
# print(get_last_high(100,10))

# def get_meter(hight,times):
#     s = 0
#     for _ in range(times):
#         s += hight
#         hight /=2
#         s+=hight
#     return s
# print(get_meter(100,10))


# def get_zhiyinshu(n):
#     l=[]
#     while n >1:
#         for i in range(2,n+1):
#             if n % i ==0:
#                 l.append(i)
#                 n = int(n/i)
#                 break
#     return l

# def print_zhiyinshu(n):
#     l1 = get_zhiyinshu(n)
#     l2 = [str(x) for x in l1]
#     s = "*".join(l2)
#     print(n,"=",s)
# print_zhiyinshu(90)



# def get_zhishu(n):
#     l=[]
#     while n> 1:                 #当n大于１　肯定有质因数
#         for i in range(2,n+1):    #遍历　２　到　ｎ的值　来被除
#             if n % i ==0:       #如过能除尽则为质因数　则添加　
#                 l.append(i)
#                 n = int(n/i)     #除过之后保留下除过的数来再此从头开始除　直到没有  
#                 break        #跳出循环　进入下一轮
#     return l

# def print_zhishu(n):
#     l1 = get_zhishu(n)          #调用函数　输入一个值得到列表
#     l2 = [str(x) for x in l1]   #把列表变为字符串
#     s = "*".join(l2)            #用　＊　号拼接字符串
#     print(n,"=",s)
# print_zhishu(90)                #调用输出函数



# import random
# s = random.sample(range(1,10),6)
# # print(s)
# f = [str(x) for x in s]
# # print(f)
# v = "".join(f)
# print(v)

#  打印杨辉三角


# def get_next_line(L):
#     '''L代表当前一行
#     返回当前行的下一行
#     如: L = [1, 2, 1]

#     返回   [1, 3, 3, 1]
#     '''
#     # 最左侧加一个1
#     rl = [1]  # 准备要返回的列表
#     # 中间 加 len(L)-1个数
#     for i in range(len(L)-1):
#         rl.append(L[i] + L[i + 1])
#     # 最右侧加一个1
#     rl.append(1)
#     return rl

# def get_yanhui_list(n):  # n代表行数
#     '''返回: [
#         [1],
#         [1, 1],
#         [1, 2, 1],
#         ...
#     ]'''
#     rl = []  # 此列表用于返回
#     line = [1]  # 当前要处理的一行
#     for _ in range(n):
#         rl.append(line)  # 把当前行放进去
#         line = get_next_line(line)
#     return rl

# def get_yanghui_string(L):
#     ''' 如果L = [[1], [1, 1], [1, 2, 1]]
#     返回rl = ["1", "1 1", "1 2 1"]
#     '''
#     rl = []
#     for line in L:
#         # 把 line=[1, 2, 1] 转为line=['1', '2', '1']
#         line = [str(x) for x in line]
#         s = ' '.join(line)
#         rl.append(s)
#     return rl

# def print_yanghui_triangle(n):
#     # 打印n行的杨辉三解
#     L = get_yanhui_list(n)
#     SL = get_yanghui_string(L)  # 字符串列表
#     # 求最大长度:
#     max_len = len(SL[-1])
#     for line in SL:
#         print(line.center(max_len))


# print_yanghui_triangle(10)


# def get_next_line(L):
#     """L代表前一行
#     返回当前行的下一行
#     如：
#         Ｌ＝【１，２，１】
#     返回【１，３，３，１】
#     """
#     #最左侧加个１
#     rl=[1] #准备要返回的列表
#     #中间　加 len(L) - 1　个数
#     for i in range(len(L)-1):
#         rl.append(L[i]+L[i+1])
#     #最右侧加１
#     rl.append(1)
#     return rl


# def get_list(n):
#     """返回[
#         [1]
#         [1,1]
#         [1,2,1]
#         ...
#     ]
#     """
#     rl = []
#     line=[1] #当前要处理的一行
#     for _ in range(n):
#         rl.append(line) #把当前放进去
#         line = get_next_line(line)
#     return rl

# def get_yanghui_string(L):
#     """如果L =[[1],[1,1],[1,2,1]]
#     返回rl = ["1","1 1","1 2 1"""
#     rl =[]
#     for line in L:
#         line = [str(x) for x in line]
#         s = " ".join(line)
#         rl.append(s)
#     return rl

# def print_yanghui(n):
#     L = get_list(n)
#     SL = get_yanghui_string(L)
#     max_len =len(SL[-1])
#     for line in SL:
#         print(line.center(max_len))

# print_yanghui(10)

# # print(get_list(10))


# def get_next_line(L):
#     """L代表前一行
#     返回当前行的下一行
#     如：
#         Ｌ＝【１，２，１】
#     返回【１，３，３，１】
#     """
#     #最左侧加个１
#     rl=[1] #准备要返回的列表
#     #中间　加 len(L) - 1　个数
#     for i in range(len(L)-1):
#         rl.append(L[i]+L[i+1])
#     #最右侧加１
#     rl.append(1)
#     return rl


# def get_list(n):
#     """返回[
#         [1]
#         [1,1]
#         [1,2,1]
#         ...
#     ]
#     """
#     rl = []
#     line=[1] #当前要处理的一行
#     for _ in range(n):
#         rl.append(line) #把当前放进去
#         line = get_next_line(line)
#     return rl

# def get_yanghui_string(L):
#     """如果L =[[1],[1,1],[1,2,1]]
#     返回rl = ["1","1 1","1 2 1"""
#     rl =[]
#     for line in L:
#         line = [str(x) for x in line]
#         s = " ".join(line)
#         rl.append(s)
#     return rl

# def print_yanghui(n):
#     L = get_list(n)
#     SL = get_yanghui_string(L)
#     max_len =len(SL[-1])
#     for line in SL:
#         print(line.center(max_len))

# print_yanghui(1)


# alist = ["hello","word"]
# for x,y in enumerate(alist):
#     print("index",x,":",y)


# def get_next_line(L):
#     rl=[1]
#     for x in range(len(L)-1):
#         rl.append(L[x]+L[x+1])
#     rl.append(1)
#     return rl

# def get_list(n):
#     rl=[]
#     line=[1]
#     for _ in range(n):
#         rl.append(line)
#         line=get_next_line(line)
#     return rl
# def get_yanghui_string(L):
#     rl=[]
#     for line in L:
#         line = [str(x) for x in line]
#         s = " ".join(line)
#         rl.append(s)
#     return rl

# def print_yanghui(n):
#     L = get_list(n)
#     SL=get_yanghui_string(L)
#     max_len = len(SL[-1])
#     for line in SL:
#         print(line.center(max_len))
# print_yanghui(2)




# def get_next_line(L):
#     rl=[1]
#     for x in range(len(L)-1):
#         rl.append(L[x]+L[x+1])
#     rl.append(1)
#     return rl


# def get_list(n):
#     rl = []
#     line = [1]
#     for _ in range(n):
#         rl.append(line)
#         line = get_next_line(line)
#     return rl


# def get_yanghui_string(L):
#     rl = []
#     for line in L:
#         line = [str(x) for x in line]
#         s = " ".join(line)
#         rl.append(s)
#     return rl

# def print_yanghui(n):
#     L=get_list(n)
#     SL = get_yanghui_string(L)
#     max_ = len(SL[-1])
#     for line in SL:
#         print(line.center(max_))

# print_yanghui(5)



# try:
#     f = open("myfile.txt","rb")
#     print("新打开的文件的读写位置:",f.tell())
#     b = f.read(2)
#     print("读取俩个位置后: ",f.tell())
#     print("读取的内容:", b)
#     # f.seek(5,0)  #0　从头向后　５个
#     # f.seek(3,1)  #１　从当前向后３个
#     f.seek(-15,2)   # 2 从后向前　１５个
#     print("移动后的位置", f.tell())
#     b1 = f.read(5)
#     print()
# except OSError:
#     print("打开文件失败")

# try:
#     f=open("a.txt","w")
#     f.write("asdas")
#     f.close()
# except OSError:
#     print("打开文件失败")

# def get_infos():
#     l=[]
#     while 1:
#         n = input("请输入姓名: ")
#         if not n:
#             break
#         p = int(input("请输入电话: "))
        
#         d = dict(name=n,phone=p)
#         l.append(d)
#     return l

# def save_infos(L):
#     try:
#         f = open("infos.txt","w")
#         for d in L:
#             f.write(d["name"])
#             f.write(" ")
#             f.write(str(d["phone"]))
#             f.write("\n")
#         f.close()
#     except OSError:
#         print("打开文件失败")

# L = get_infos()
# save_infos(L)

# def read_infos()

##求完全数
# l=[]
# for x in range(1,1000):
#     for y in range(1,x):
#         if x % y == 0:
#             l.append(y)
#     if sum(l) == x:
#         print(l)
#         print(x)
#     l=[]

# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.money = 0
#         self.skill = []
#     def teach(self,other,skill):
#         print(self.name,"教",other.name,"学",skill)
#         other.skill.append(skill)
#     def work(self,money):
#         print(self.name,"上班赚了",money)
#         self.money += money
#     def borrw(self,other,money):
#         self.money += money
#         other.money -= money
#     def show_info(self):
#         print(self.age,"岁的",self.name,"有钱：",self.money,"他学会的技能是:",self.skill)



# zhang3 =Human("张三","35")
# li4 = Human("李四","8")
# zhang3.teach(li4,"Python")
# li4.teach(zhang3,"王者荣耀")
# zhang3.work(1000)
# li4.borrw(zhang3,200)
# zhang3.show_info()
# li4.show_info()


# class Student:
#     def __init__(self,name,age,score=0):
#         self.name = name
#         self.age =age
#         self.score = score
    
#     def set_score(self,score):
#         self.score =score
    
#     def show_info(self):
#         print(self.name,"今年",self.age,"成绩是: ",self.score)

# l=[]
# l.append(Student("陈华齐",21,100))
# l.append(Student("张奔",21,100))
# l.append(Student("小胖",21))
# l.append(Student("安付伟",21,100))
# for i in l:
#     i.show_info()
# l[-2].set_score(90)
# for s in l:
#     s.show_info()

# try:
#     f = open("a.txt","w")
#     while 1:
#         n = input("请输入姓名: ")
#         if not n:
#             break
#         p = int(input("请输入电话: "))

    
#         f.write(n)
#         f.write(" ")
#         f.write(str(p))
#         f.write("\n")
# except OSError:
#     print("打开文件失败")

# # 1. 打开文件
# myfile = open("a.txt")


# # 2. 读取文件数据,并打印为相应格式
# # 方法1,每次读取一行,然后进行处理后打印
# while True:
#     line = myfile.readline()
#     if line == '':
#         break
#     line = line.strip()  # 去掉末尾的'\n'
#     L = line.split()  # 将其拆分为字符串列表
#             # L=['小李', '13888888888']
#     print('姓名:', L[0], "电话:", L[1])

# # 3. 关闭文件
# myfile.close()

# try:
#     f = open("a.txt")
#     while 1:
#         s1= f.readline()
#         if not s1:
#             break
#         s1 = s1.strip()
#         l = s1.split()
#         print("姓名",l[0],"电话",l[1])
#     f.close()
# except OSError:
#     print("打开文件失败")

# try:
#     f = open("a.txt")
#     while 1:
#         s = f.readline()
#         if not s:
#             break
#         s = s.strip()
#         l = s.split()
#         print("姓名",l[0],"电话",l[1])
#     f.close()
# except OSError:
#     print("打开文件失败")

# try:
#     f = open("infos.txt","w")
#     try:
#         while 1:
#             n = input("请输入姓名: ")
#             if not n:
#                 break
#             a = int(input("请输入年龄:"))
#             d = input("请输入地址")
#             f.write(n)
#             f.write(" ")
#             f.write(str(a))
#             f.write(" ")
#             f.write(d)
#             f.write("\n")
    
#         f.close()
#     except ValueError:
#         print("输入值有问题已处理")
# except OSError:
#     print("打开文件失败")

# try:
#     f1 = open ("infos.txt")
#     while 1:
#         s=f1.readline()
#         if not s:
#             break
#         s = s.strip()
#         l = s.split()
#         print("姓名",l[0],"年龄",l[1],"地址",l[2])
#     f.close()

# except OSError:
#     print("打开文件失败")
# import time
# def mycopy(use,get):
#     try:
#         f1 = open(use,"rb")
#         try:
#             try:
#                 f2 = open(get,"wb")
#                 try:
#                     while 1:
#                         data=f1.read(4096)
#                         if not data:
#                             break
#                         f2.write(data)
#                     time.sleep(2)
#                     print("复制成功")
#                 finally:
#                     f2.close()
#             finally:
#                 f1.close()
#         except OSError:
#             print("复制失败")
#     except OSError:
#         print("复制失败")
# n = input("请输入源文件: ")
# s = input("请输入目标文件: ")
# mycopy(n,s)


# s = {'唐僧', '悟空', '八戒','沙僧'}

# it = iter(s)
# try:
#     while 1:
#         print(next(it))
# except StopIteration:
#     print("遍历结束")

# def myeven(start,stop):
#     if start % 2  == 1:
#         start += 1
#     for i in range(start,stop,2):
#         yield i

# for x in myeven(3,20):
#     print(x)


# def myfactorial(n):
#     s = 1
#     for x in range(1,n+1):
#         s *= x
#         yield s
# # l = list(myfactorial(5))
# # print(l)
# for x in myfactorial(5):
#     print(x)


# gen = (x**2 for x in range(1"MyNumber(%d)" % ,10))
# for x in gen:
#     print(x)

# print((x for x in (x**2 for x in range(1,10))))


# l = [2,3,5,7]
# def myfun(n):
#     for x in n:
#         yield x**2+1
# for x in myfun(l):
#     print(x)

# gen = (x for x in (x**2+1 for x in l))
# for x in gen:
#     print(x)

# gen= [x for x in (x**2+1 for x in l)]
# print(gen)
# l = []
# while 1:

#     n = input("请输入: ")
#     if not n:
#         break
#     l.append(n)
# print(l)
# for t in enumerate(l,1):
#     print("第%s行:%s" % t)
    
# def prime(begin,end):
#     for x in range(begin,end):
#         if x < 2:
#             continue
#         for y in range(2,x):
#             if x % y == 0:
#                 break
#         else:
#             yield x
# l = [x for x in prime(1,5)]
# print(l)

# l = []
# for x in range(1,100000):
#     for y in range(1,x):
#         if x % y == 0:
#             l.append(y)
#     if sum(l) == x:
#         print(l)
#         print(sum(l))
#     l=[]

# l = []
# for x in range(1,1000):
#     for y in range(1,x):
#         if x % y ==0:
#             l.append(y)
#     if sum(l) == x :
#         print(x)
#     l=[]


# def get_age():
#     n = int(input("请输入年龄（１－１４０）: "))
#     if n <0 or n >140:
#         raise ValueError
#     return n
# try:
#     n = get_age()
#     print(n)
# except ValueError:
#         print(0)


# def fet_age():
#     n = int(input("请输入:"))
#     assert 1<= n <=140,"值错误"
#     return n

# try:
#     n = fet_age()
#     print(n)
# except AssertionError as err:
#     print("错误类型",err)




# import time
# HH = int(input("请输入小时: "))
# MM = int(input("请输入分钟: "))
# SS = int(input("请输入秒数： "))
# while 1:
#     t =time.localtime()
#     hh = t[3]
#     mm = t[4]
#     ss = t[5]
#     print("%0d:%0d:%0d" % (hh,mm,ss))
#     time.sleep(1)
#     if hh ==HH and mm == MM and ss ==SS:
#         print("时间到!!!")
#         break


# from math import factorial as fac
# def fun(n):
#     s = 1
#     for x in range(1,n+1):
#         s += 1/fac(x)
#     print(s)

# fun(500)
# def myfun(n):
#     s = 0
#     for x in range(1,n+1):
#         s += ((-1)**(x+1))/(2*x-1)
#     return s
# s = myfun(10000000)
# print(s*4)


# a = ["\u2660","\u2663","\u2666","\u2665"]
# l1 = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# l2=[]
# for x in a:
#     for y in l1:
#         l2.append(x+y)
# l2.append("大王")
# l2.append("小王")
# # print(l2)
# import random
# import time
# s = random.shuffle(l2)


# n = input("请按回车发牌: ")
# if not n:
#     print("正在发牌....")
#     time.sleep(1)
#     s1 = l2[:17]
#     print("第一个人的牌:",s1)
# n1 = input("请按回车发牌：")
# if not n1:
#     print("正在发牌....")
#     time.sleep(1)
#     s2 = l2[17:34]
#     print("第二人的牌:",s2)
# n2 = input("请按回车发牌: ")
# if not n2:
#     print("正在发牌...")
#     time.sleep(1)
#     s3 = l2[34:51]
#     print("第三个人牌:",s3)
# n3 = int(input("请抢地主: "))
# if n3 == 1:
#     print("底牌为:",l2[51:54])
#     s1.extend(l2[51:54])
#     print("第一个人的牌:",s1)
#     print("第二个人的牌:",s2)
#     print("第三个人的牌:",s3)
# if n3 == 2:
#     print("底牌为:",l2[51:54])
#     s2.extend(l2[51:54])
#     print("第一个人的牌:",s1)
#     print("第二个人的牌:",s2)
#     print("第三个人的牌:",s3)

# if n3 == 3:
#     print("底牌为:",l2[51:54])
#     s3.extend(l2[51:54])
#     print("第一个人的牌:",s1)
#     print("第二个人的牌:",s2)
#     print("第三个人的牌:",s3)
        

# def get_next_line(L):
#     l=[1]

#     for x in range(len(L)-1):
#         l.append(L[x]+L[x+1])
#     l.append(1)
#     return l

# # print(get_next_line([1,3,3,1]))
# #第二步　得到[[1],[1,1],[1,2,1]]
# def get_list(n):
#     l =[]
#     line =[1]
#     for _ in range(n):
#         l.append(line)
#         line = get_next_line(line)
#     return l
# # print(get_list(2))

# #第三步返回　列表字符串　["1","1 1","1 2 1"]

# def get_yanghui_string(L):
#     l = []
#     for line in L:
#         line = [str(x) for x in line]
#         s = " ".join(line)
#         l.append(s)
#     return l
# L = [[1],[1,2,1]]
# print(get_yanghui_string(L))

# def print_yanghui_triangle(n):
#     s = get_list(n)
#     sl = get_yanghui_string(s)
#     max_len = len(sl[-1])
#     for x in sl:
#         print(x.center(max_len))

# print_yanghui_triangle(5)

# def mysum(n):
#     s = 0
#     for x in range(n+1):
#         s += x
#     return s
# print(mysum(10

# import math
# def myfun(n):
#     return math.factorial(n)
# print(myfun(5))

# def mysum(n):
#     s = 0
#     for x in range(1,n+1):
#         s += x**x
#     return s
# print(mysum(10))


# def get_chinese_char_coubt(s):
#     l = []
#     for x in s:

#         if 0x4e00 < ord(x) < 0x9FA45:
#             l.append(x)
#     return len(l)
# s = input("请输入中英文混合字符串: ")
# print("中文个数为:",get_chinese_char_coubt(s))


# def isprime(x):

#     if x < 2:
#         return False
#         for k in range(1,x+1):
#             if i % k ==0:
#                 return False
#     else:
#         return True


# def prime_m2n(m,n):
#     l = []
#     for x in range(m,n):
#         if isprime(x):
#             l.append(x)
#     return l

# print(prime_m2n(10,20))

# l =[[1,2,3,4],[1,2,3,4,5,6]]
# for x in l:
#     x = [str(x) for x in l] 

# s1=" ".join(l)

# print(s1)

# l = [1,2,3,4]
# l1 = []
# for x in l:
#     s = [str(x) for x in l]
# print(s)
# s1 = " ".join(s)
# l1.append(s1)
# print(l1)

# l = "chen hua qi"
# s = l.split()
# print(s)

# l = "chenhauqi"
# s1 = " ".join(l)
# print(s1)
# s2 = "#".join(l)
# print(s2)



# def demo(t):
#     print([1])
#     print([1,1])
#     line=[1,1]
#     for i in range(2,t):
#         r = []
#         for j in range(0,len(line)-1):
#             r.append(line[j]+line[j+1])
#         line = [1] +r + [1]
#         print(line)
# demo(10)


# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
    
#     # def describe_restaurant(self):
#     #     print("餐馆名字叫: ",self.restaurant_name,"正在营业")
    
#     # def open_restaurant(self):
#     #     print("您点的菜是",self.cuisine_type)
    
#     def show_info(self):
#         print("饭店名字叫:",self.restaurant_name,"您点的菜为:",self.cuisine_type)

    

# restaurant = Restaurant("和平饭店","大杂烩")
# restaurant.show_info()

# class Sweetpotato:

#     def __init__(self):
#         self.cookedString = "生的"
#         self.cookedlevel = 0
#         self.condiments = []
#     def __str__(self):
#         return "地瓜状态:%s(%d),添加了%s" % (self.cookedString,self.cookedlevel,str(self.condiments))
#     def cooked(self,cooked_time):
#         self.cookedlevel += cooked_time
#         if self.cookedlevel >=0 and self.cookedlevel <3:
#             self.cookedString = "生的"
#         elif self.cookedlevel >= 3  and self.cookedlevel<5:
#             self.cookedString ="半生不熟"
#         elif self.cookedlevel >=5 and self.cookedlevel < 8:
#             self.cookedString ="熟了"
#         elif self.cookedlevel > 8:
#             self.cookedString = "糊了"
#     def addcondiments(self, what):
#         self.condiments.append(what)
# di_gua = Sweetpotato()
# print(di_gua)

# di_gua.cooked(5)
# print(di_gua)
# di_gua.addcondiments("大蒜")
# di_gua.addcondiments("孜然")
# di_gua.addcondiments("芥末")
# print(di_gua)


# class Home:
#     def __init__(self,new_area,new_info,new_addr):
#         self.area = new_area
#         self.info = new_info
#         self.addr = new_addr
#         self.left_area = new_area
#         self.totle_jiaju = []
#     def __str__(self):
#         msg = "房子的总面积%d,可用面积：%d,户型:%s,地址:%s" % (self.area,self.left_area,self.info,self.addr)
#         msg += "当前房子家具有：%s" % (str(self.totle_jiaju))
#         return msg
#     def add_jiaju(self,jiaju):
#         self.left_area -= jiaju.get_area()
#         self.totle_jiaju.append(jiaju.get_name())
# class Bed:
#     def __init__(self,new_name,new_area):
#         self.name = new_name
#         self.area = new_area
#     def __str__(self):
#         return "床的品牌:%s,床的面积:%d" % (self.name,self.area)
#     def get_area(self):
#         return self.area
#     def get_name(self):
#         return self.name


# fangzi = Home(90,"三室一厅","杭州市　余杭区　旭辉府")
# print(fangzi)

# bed1 = Bed("席梦思",4)
# print(bed1)
# bed2 = Bed("三人床",6)
# print(bed2)
# fangzi.add_jiaju(bed2)
# fangzi.add_jiaju(bed1)
# print(fangzi)


# class Dog:
#     def __send_msg(self):
#         print("正在发送短信")
#     def send_msg(self,new_money):
#         if new_money > 100:
#             self.__send_msg()
#         else:
#             print("余额不足")

# t1 = Dog()
# t1.send_msg(1000)


# class Dog:
#     def __del__(self):
#         print("---gameover----")

# t1 = Dog()
# t2 = t1
# t3 = Dog()
# del t1
# # del t2
# del t3
# print("--------------------")
# class Dog:
#     def bark(self):
#         print("---汪汪叫----")

# class xiaotq(Dog):
#     def fiy(self):
#         print("－－－－飞－－－－")
#         Dog.bark(self)

# tq = xiaotq()
# tq.fiy()

# class CarStore(object):

#     def __init__(self):
#         self.factory = Factory()

#     def order(self,car_type):
#         return self.factory.your_car(car_type)
# class Factory(object):
#     def your_car(self,car_type):
#         if car_type == "保时捷":
#             return Baoshijie()
#         elif car_type == "宝马":
#             return Bmw("宝马")
#         elif car_type == "ix35":
#             return Ix35()


# class Car(object):
#     def __init__(self,new_name):
#         self.name = new_name

#     def move(self):
#         print(self.name,"在移动...")
#     def music(self):
#         print(self.name,"在播放音乐")
#     def stop(self):
#         print(self.name,"正在停下")
# class Baoshijie(Car):
#     pass
# class Bmw(Car):
#     pass
# class Ix35(Car):
#     pass

# car_store = CarStore()
# car = car_store.order("宝马")
# car.move()
# car.music()
# car.stop()

class CarStore(object):

    def __init__(self):
        self.factory = Factory()

    def order(self,car_type):
        return self.factory.your_car(car_type)
class Factory(object):
    def your_car(self,car_type):
        if car_type == "保时捷":
            return Baoshijie()
        elif car_type == "宝马":
            return Bmw("宝马")
        elif car_type == "ix35":
            return Ix35()


class Car(object):
    def __init__(self,new_name):
        self.name = new_name

    def move(self):
        print(self.name,"在移动...")
    def music(self):
        print(self.name,"在播放音乐")
    def stop(self):
        print(self.name,"正在停下")
class Baoshijie(Car):
    pass
class Bmw(Car):
    pass
class Ix35(Car):
    pass

car_store = CarStore()
car = car_store.order("宝马")
car.move()
car.music()
car.stop()



