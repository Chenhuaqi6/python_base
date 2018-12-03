# class myrange:
#     def __init__(self,start,stop = None,step = 1):
#         if stop is None:
#             stop = start
#             start = 0
#         self.start = start
#         self.stop = stop
#         self.step = step
    
#     def __iter__(self):
#         return MyrangeIterator(self.start,self.stop,self.step)


# class MyrangeIterator:
#     def __init__(self,start,stop,step):
#         self.start = start
#         self.stop = stop
#         self.step = step
#     def __next__(self):
#         if self.step > 0:
#             while self.start < self.stop:
#                 r = self.start  #要返回的值
#                 self.start += self.step
#                 return r
#             else:
#                 raise StopIteration
#         if self.step < 0:
#             while self.start > self.stop:
#                 r = self.start
#                 self.start += self.step
#                 return r
#             else:
#                 raise StopIteration
#         else:
#             raise StopIteration
# for x in myrange(10,1,-2):
#     print(x)





class myrange:
    def __init__(self,start,stop = None,step = 1):
        if stop is None:
            stop = start
            start = 0
        self.start = start
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return MyrangeIterator(self.start,self.stop,self.step)


class MyrangeIterator:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step
    def __next__(self):
        if self.step > 0:
            while self.start < self.stop:
                r = self.start  #要返回的值
                self.start += self.step
                return r

        if self.step < 0:
            while self.start > self.stop:
                r = self.start
                self.start += self.step
                return r

       
        raise StopIteration
for x in myrange(10,1,-2):
    print(x)