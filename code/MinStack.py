# insertion sort with min stack
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min=[]
        self.s=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        if len(self.min)==0:
            self.min.append(x)
        elif x <= self.min[-1]:
            self.min.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        a=self.s.pop()
        if a == self.getMin():
            self.min.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()