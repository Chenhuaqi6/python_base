#此示例示意作用域

v = 100
def f1():
    # v = 200
    print("f1=", v)
    def f2():
        # v = 300
        print("f2=", v)
    f2()
f1()
print("v=",v)