#此示例示意当zip 有俩个参数时，实现自定义的myzip函数


def myzip(iter1,iter2):
    #先得到俩个可迭代对象的迭代器
    it1 = iter(iter1)
    it2 = iter(iter2)
    while 1:
        try:
            x = next(it1)
            y = next(it2)
            yield (x,y)
        except StopIteration:
            return

numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']
for t in myzip(numbers, names):
    print(t)