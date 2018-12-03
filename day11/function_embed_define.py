

# def fn_outer():
#     print("fn_outer被调用")
#     def fn_inner():
#         print("fn_inner被调用")
#     print("fn_outer调用结束")
# fn_outer()
# fn_inner()  #调用出错

#此示例示意在函数内部创建函数，在函数外部来调用内部的函数
# def fn_outer():
#     print("fn_outer被调用")
#     def fn_inner():
#         print("fn_inner被调用")
#     print("fn_outer调用结束")
#     return fn_inner
# fx=fn_outer()
# fx()

# def fn(a,b,*args,c,**kwargs):
#         pass
        
# fn(1,2,3,4,c=30,d=40,e=50)

# def fn(a,b,*args,c,**kwargs):
#     pass
    
# fn(1,2,3,4,c=30,d=40,e=50)
def func(a,b,*args,*,c,d):
    print(a,b,args,c,d)
func(1,2,3,5,4,c=10,d=20)