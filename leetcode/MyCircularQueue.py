class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.q = collections.deque([])
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if len(self.q)<self.size:
            self.q.append(value)
            return True
        else:
            return False
        

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if len(self.q)>0:
            self.q.popleft()
            return True
        else:
            return False
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if len(self.q)>0:
            return self.q[0]
        else:
            return -1
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        
        if len(self.q)>0:
            return self.q[-1]
        else:
            return -1
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if len(self.q)==0:
            return True
        else:
            return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return len(self.q)==self.size        

