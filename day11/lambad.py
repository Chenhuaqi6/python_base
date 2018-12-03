#此示例示意lambad表达式的用法和语法

# def myadd(x,y):
#     return x + y
#用lambad表达式来创建上面的函数
# myadd = lambda x, y:x+y
# print("20+30=", myadd(20,30)) #50
# print("4+5=", myadd(4,5))


# fx = lambda n: True if (n**2+1) % 5 == 0 else False 

# print(fx(3))
# print(fx(4))

# fx = lambda n: (n**2+1) % 5 == 0
# print(fx(3))
# print(fx(4))


# mymax = lambda x,y:max(x,y)
# print(mymax(100,200))

# mymax = lambda x,y:x if x>y else y
# print(mymax(100,200)) 

# def fx(f,x,y):
#     print(f(x,y))
# fx((lambda a,b: a+b),100,200)
# fx((lambda x,y: x**y),3,4)

# fx = lambda x:x*3
# print(fx(3))
# print((lambda x:x*5,range(1,5)))

def fx(f,x,y):
    print(f(x,y))
fx((lambda a,b:a+b),100,200)
fx((lambda x,y:x**y),3,4)