#此示例示意装饰器的用途和作用
#模拟银行项目
#业务: 　存钱和取钱

def privileged_check(fn):
    def fx(n, yuan):
        print("正在检查权限．．．通过！")
        fn(n, yuan)#调用被装饰函数
        print("感谢使用")
    return fx
def send_message(fn):
    def fy(n,x):
        fn(n,x)
        print("正在发送给．．．", n)
    return fy

#---------chen------------
@privileged_check     
def savemoney(name,x):
    print(name,"存钱",x,"元")
    
@privileged_check
@send_message
def withdraw(name,x):
    print(name,"取钱",x,"元")

#--------ｚｈａｎｇ－－－－－－－－－－－
savemoney("小王",200)
savemoney("小赵",400)

withdraw("小钱",500)