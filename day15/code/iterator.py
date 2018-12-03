# L = [2,3,5,7]
# it = iter(L)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))  #异常


# l=[2,3,5,7]
# #1 for
# for x in l:
#     print(x)

# print("-----------------")

# myit = iter(l) #从l中拿到迭代器，用myit来绑定
# while True:
#     try:
#         x = next(myit)
#         print(x)

#     except StopIteration:
#         break   #结束循环不再向迭代器获取数据了


# 练习：
#     有一个集合
#         s = {"唐生","悟空","八戒","沙僧"}
#         用ｆｏｒ　语句来遍历所有元素如下：
#             for x in s:
#                 print(x)
#             else:
#                 print("遍历结束)
#         #将for 改成while 和迭代器


s = {"唐生","悟空","八戒","沙僧"}
myit = iter(s)
while True:
    try:
        x = next(myit)
        print(x)
    except StopIteration:
        print("遍历结束")
        break
# i = 0
# l = list(s)
# while i < len(l):
#     print(l[i])
#     i += 1
# print("遍历结束")
