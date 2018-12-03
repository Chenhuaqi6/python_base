class MyList:
    def __init__(self,interable=()):
        # self.data = list(interable)
        self.data = [x for x in interable]
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __add__(self,rhs):
        return MyList(self.data + rhs.data)
    def __iadd__(self,rhs):
        print("__iadd__被调用")
        self.data.extend(rhs.data)
        return self  #返回自身
    def __neg__(self):
        a = [-x for x in self.data]
        return MyList(a)
    def __contains__(self,e):
        return e in self.data

l1 = MyList([1,2,3])
l2 = MyList([4,5,6])
l = MyList([1,-2,3,-4,5])
l7 = -l
print(l7)
l1 += l2
print(l1)
s = l1.__add__(l2)
print(s) 
print(3 in l1)

