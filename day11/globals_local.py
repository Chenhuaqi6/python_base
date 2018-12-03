#示意globals() 和　locals 函数的用法

a = 1
b = 2
c = 3
def fn(c,d):
    e = 300
    print("locals()返回", locals())
    print("glocals()返回", globals())

    print(a,b,c,d,e)
    print("全局变量c的值", globals()["c"])
fn(100,200)
