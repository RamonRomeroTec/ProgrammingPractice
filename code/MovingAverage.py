from collections import deque
class MovingAverage(object):
    def __init__(self, size):
        self.s=size
        self.l=deque([])
        self.sum=0
    def next(self, val):
        if len(self.l)==self.s:
            self.sum-=self.l.popleft()
        self.sum+=val
        self.l.append(val)        
        return float(self.sum)/float(len(self.l))
   