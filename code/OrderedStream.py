class OrderedStream:

    def __init__(self, n):
        self.a=[None]*n
        self.ptr=0
        

    def insert(self, id, value):
        self.a[id-1]=value
        s=[]
        while self.ptr < len(self.a):
            if self.a[self.ptr] == None:
                return s
            else:
                s.append(self.a[self.ptr])
                self.ptr+=1
        return s


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)