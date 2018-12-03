#try_excpet.py

# def div_apple(n):
#     print("%d个苹果想分给几个人？" % n)
#     s = input("请输入人数: ")
#     count = int(s)       #ValueError错误
#     result = n / count   #可能触发ZeroEivisionErorr
#     print("每人分了", result ,"个苹果")

# div_apple(10)
# print("程序结束")


# def div_apple(n):
#     print("%d个苹果想分给几个人？" % n)
#     s = input("请输入人数: ")
#     count = int(s)       #ValueError错误

#     result = n / count   #可能触发ZeroEivisionErorr
#     print("每人分了", result ,"个苹果")
# try:
#     div_apple(10)
#     print("分苹果成功")
# except ValueError as err:   #err绑定ValueError  err 中存有错误信息　在此处能知道用户输入的什么导致的错误
#     print("div_apple函数内部发生错误，已处理，程序恢复正常状态")
#     print("错误起因: ", err)
# except ZeroDivisionError:

#     print("用户输入的人数为０，程序已恢复正常状态")
#     print("每人取苹果，苹果被收回")
# print("程序结束")

# def div_apple(n):
#     print("%d个苹果想分给几个人？" % n)
#     s = input("请输入人数: ")
#     count = int(s)       #ValueError错误
#     result = n / count   #可能触发ZeroEivisionErorr
#     print("每人分了", result ,"个苹果")
# try:
#     div_apple(10)
#     print("分苹果成功")
# except ValueError:   #此处只捕获Value错误
#     print("苹果不分了")
# except:
#     #此处能够捕获除ValueError以外的全部错误
#     print("except　子句被执行，程序已转入正常状态")
#     #注:except 子句只能写在所有except之后
# else:  #此语句只有在try中没有发生任何异常时才会执行
#     print("没有错误，程序直接执行")
# finally:
#     #此处的语句，只要离开此try语句，则此处的语句一定会被执行
#     print("我一定会被执行")
# print("程序结束")



# 小练习
# 写一个函数，get_scroe() 来获取学生输入的成绩信息（０－１００）的整数，如果输入出现异常，则此函数返回０，否则返回用户输入的成绩
def get_scoer():
    try:
        n = int(input("请输入成绩(0-100):"))
        if 0<= n <= 100:
            return n

    except ValueError:
        return 0
scoer = get_scoer()
print("学生的成绩为:", scoer)