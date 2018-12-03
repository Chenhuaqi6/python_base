# def get_chinese_char_count(s):
#     count = 0
#     for i in s:
#         if 0x4E00 < ord(i) < 0x9FA45:
#             count += 1
#     return count
# s = input("请输入中文英文混合的字符串: ")
# print("您输入的中文个数是: ", get_chinese_char_count(s))


def isprime(x):
    if x < 2:
        return False
    #此处ｘ一定大于等于２
    for i in range(2,x):
        if x % 1 == 0:
            return False
    return True




# def myrange(start,stop=None,step=1):
    #先判断stop是否为None