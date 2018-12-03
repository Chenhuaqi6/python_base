# s = input('请输入字符串')
# if s:
#     print('第一个字符是',s[0])
#     print('最后一个字符是',s[-1])
#     if len(s) % 2 == 1:
#         center = int(len(s) // 2)
#     print('中间这个字符是：',s[center])
# else:
#     print("您输入的字符串有误")


# 输入字符串　切掉第一个和最后一个
# s = input("请输入一个字符串: ")
# if s:
#     print("切片后的字符串", s[1:(len(s)-1)] )



s = input("请输入一行文字：　")
s2 = s[::-1]
if s == s2:
    print(s, "是回文")
else:
    print(s, "不是回文")