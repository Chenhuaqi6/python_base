#try-finally语句


# def fry_egg():
#     print("打开天然气．．．")
#     try:
#         count = int(input("请输入鸡蛋个数: "))
#         print("完成煎鸡蛋，共煎了%d个鸡蛋！" % count)
#     finally:    
#         print("关闭天然气")

# try:
#     fry_egg()
# except ValueError as err:
#     print("发生值的错误，以处理并转为正常状态")
# print("程序结束")




# def get_number():
    
#     s = input("请输入整数: ") or "0"
#     i = int(s)
#     return i
# try:
#     print(get_number())
    
# except ValueError as err:
#     print("发生错误，已转为正常状态")
#     print("错误类型", err)
# except:
#     print("错误转正常")
# print(get_number())
def get_number():
    s = input("请输入: ")
    try:
        i = int(s)
    except:
        i = 0
    return i
print(get_number())




    