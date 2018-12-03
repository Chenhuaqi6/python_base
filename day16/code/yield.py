##yield.py


# def myyield():
#     yield 2
#     yield 3
#     yield 5
#     yield 7
#     print("生成结束")
# r=myyield()　#r 绑定生成器
# it = iter(r) #拿到生成器的迭代器
# try:
#     print(next(it))     #　２　向生成器获取数据
#     print(next(it))     #　３　向生成器获取数据
#     print(next(it))     #　５　向生成器获取数据
#     print(next(it))     #　７　向生成器获取数据
#     print(next(it))     #　　stopiteration 通知生成结束
# except StopIteration:
#     print("程序错误，已解决")


# def myyield():
#     yield 2
#     yield 4
#     yield 6
#     yield 8
#     print("生成结束")
# for x in myyield():
#     print(x)

def myyield():
    yield 2
    yield 3
    yield 5
    yield 7
    print("生成结束")
gen = myyield()
for x in gen :
    print(x)
print("---------------------")
#生成器对象是一次性的
#一旦生成结束，将不能再重新生成数据
for x in gen:
    print(X)

for x in myyield():
    print(x)

for x in myyield():
    print(x)
