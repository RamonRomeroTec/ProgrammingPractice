class MinStack(object):

    def __init__(self):
        self.s=[]
        self.ms=[]
        
    def push(self, x):
        self.s.append(x)
        if not self.ms:
            self.ms.append(x)
        elif self.ms[-1]>=x:
            self.ms.append(x)
        

    def pop(self):
        i=self.s.pop()
        if i == self.ms[-1]:
            self.ms.pop()
        

    def top(self):
        return self.s[-1]
        

    def getMin(self):
        return self.ms[-1]
        

