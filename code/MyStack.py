from collections import deque
class MyStack(object):
    def __init__(self):
        self.q1=deque([])
        self.q2=deque([])
    def push(self, x):
        self.q1.append(x)   
    def pop(self):  
        while len(self.q1)!=1:
            self.q2.append(self.q1.popleft())
        r = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return r
    def top(self):
        while len(self.q1)!=1:
            self.q2.append(self.q1.popleft())
        r = self.q1.popleft()
        self.q2.append(r)
        self.q1, self.q2 = self.q2, self.q1
        return r
    def empty(self):
        if len(self.q1)>0:
            return False
        return True
   