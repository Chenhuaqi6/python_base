# def get_random_passwd():
#     import random
#     l=[]
#     s = "0123456789"
#     for x in range(6):
#         ch = random.choice(s)
#         l.append(ch)
#     return "".join(l)
# passwd = get_random_passwd()
# print(passwd)


import random
x = random.randrange(101)
# print(x)
count = 0
while 1:
    y = int(input("请输入: "))
    if y > x:
        print("您猜大了")
        count += 1
    elif y < x:
        print("您猜小了")
        count +=1
    elif y == x:
        print("恭喜您猜对了")
        count += 1
        break
print("共输入:",count)