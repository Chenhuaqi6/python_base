
# x**y

# def myfun(y):
#     def fun(x):
#         return x**y
#     return fun
# sd = myfun(3)
# print(sd(2))

# a**2+b*5+1

def myadd(a):
    def add(b):
        return a**2+b*5+1
    return add
sd = myadd(2)
print(sd(5))