# l = []
# for i in range(1,1000):
#     for x in range(1,i):
#         if i % x == 0:
#             l.append(x)
#     if sum(l) == i:
#         print(l)
#         print(sum(l))
#     l=[]


def is_perfect_number(x):
    L=[] #此列表用于存放　所有的因数
    for i in range(1,x):
        if x % i == 0:
            L.append(i)
    #走到此步所有的因数已存在于Ｌ中
    if sum(L) == x:
        return True
    return False





i = 1
while 1:
    if is_perfect_number(i):
        print(i)
    i += 1
    
