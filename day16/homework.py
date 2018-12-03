#   2. 写一个生成器函数myxrange([start, ], stop[, step]) 来生成一系列整数
#     要求:
#       myxrange功能与range功能相同（不允许调用range函数)


# def myrange(*args):
#     if len(args) == 1:
#         i = 0
#         while i <args[0]:
#             yield i
#             i +=1
#     if len(args) == 2:
#         i = args[0]
#         while i < args[1]:
#             yield i
#             i +=1
#     if len(args) == 3 and args[2] > 0:
#         i = args[0]
#         while i < args[1]:
#             yield i
#             i+=1+args[2]
#     if len(args) == 3 and args[2] < 0:
#         i =args[0]
#         while i > args[1]:
#             yield i
#             i += args[2]
# l = [x for x in myrange(1,10,2)]
# print(l)
# s = sum([x**2 for x in myrange(100) if x % 2 == 1 ])
# print(s)
# for x in myrange(1,10):
#     print(x)

# l=[]
# for x in myrange(100):
#     if x % 2 == 1:
#         l.append(x)
# print(l)
# s = 0
# for y in l:
#     s += y**2
# print(s)



def myfibonacci(n):
    a = 1
    b = 0
    for _ in range(n):
        a,b=b,a+b
        yield b
s = [x for x in myfibonacci(40)]
print(s)
for x in myfibonacci(40):
    print(x,end=" ")
print()
print(sum(s))
        
        


# 3. 写程序，实现复制文件功能
#   要求:
#     1) 要考虑关闭文件问题
#     2) 要考虑超大文件复制问题
#     3) 要能复制二进制文件(如:/usr/bin/python3 等文件)

def mycopy(src_filename, dst_filename):  # 源文件名和目标文件名
    try:
        fr = open(src_filename, 'rb')
        try:
            try:
                fw = open(dst_filename, 'wb')
                try:
                    while True:
                        b = fr.read(4096)
                        if not b:
                            break
                        fw.write(b)
                finally:
                    fw.close()
            except OSError:
                print("打开目标文件失败")
        finally:
            fr.close()
    except OSError:
        print("打开源文件失败")



src = input("请输入源文件名:")
dst = input("请输入目标文件名:")
mycopy(src, dst)