class MyQueue(object):
    def __init__(self):
        self.s1=[]
        self.s2=[]
    def push(self, x):
        self.s1.append(x)
    def pop(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        a = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return a
    def peek(self):
        return self.s1[0]
    def empty(self):
        if len(self.s1)==0:
            return True
        return False
    