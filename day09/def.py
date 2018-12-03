def my素数(a,b):
    l=[]
    for x in range(a,b+1):
        if x < 2:
            continue
        for i in range(2,x):
            if x % i ==0:
                break
        else:
            l.append(x)
                
    print(l)
my素数(0,32)

# #此示例示意定义一个带有形参的函数，并调用
# def mymax(a,b):
#     print("a=",a)
#     print("b=",b)
#     if a > b:
#         print("最大值是",a)
#     else:
#         print("最大值是",b)
# mymax(200,300)
# mymax(300,400)

#练习　写一个函数myadd,此函数中的参数列表里有俩个参数ｘ，ｙ　此函数功能是打印ｘ＋ｙ的和

# def myadd(x,y):
#     print("x=",x)
#     print("y=",y)
#     s = x+y
#     print("和是",s)
# myadd(100,200)
# myadd("ABC","123")


#写一个函数print_even,传入一个参数n代表终止整数打印２　４　６　８　．．．．ｎ之间的所有偶数包含（ｎ）
# def print_even(n):
#     for x in range(2,n+1,2):
#         print(x,end=" ")
# return
# return
# return
# return
# return
# return
# return
# return,300))
# return