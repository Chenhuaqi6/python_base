#实现俩个自定义的列表相加

class MyList:
    def __init__(self,interable=()):
        # self.data = list(interable)
        self.data = [x for x in interable]
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __add__(self,rhs):
        return MyList(self.data + rhs.data)
    def __mul__(self,rhs):
        return MyList(self.data * rhs)
    def __rmul__(self,lhs):
        return MyList(self.data * lhs)
    def __iadd__(self,rhs):
        return MyList(self.data += rhs.data)




l1 = MyList(range(1,4))
l2 = MyList([4,5,6])
l3 = l1 + l2
print(l3)
l4 = l2 + l1
print(l4)
l5 = l1 * 2
print(l5)
l6 = 8 * l1
print(l6)

print(l1+=l2)