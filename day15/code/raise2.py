# raise2.py


# 此示例示意raise的语法

def f1(x):
    print(x)
    #此处对ｘ进行处理，可能触发错误
    e = ValueError(str(x) + "此数值不能被处理")
    raise e


def f2(x,y):
    try:
        f1(x)
    except ValueError as err:
        print("f1函数内部有错误，已处理",err)
        raise  #raise err
    print(x,y)

     
try:
    f2(0,100)
except ValueError as err:
    print("f1函数内部有错误，已处理",err)

