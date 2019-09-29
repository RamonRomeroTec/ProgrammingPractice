# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# def recursion(list1):
#     return recursion2(0, list1, 1)

# def recursion2(sum1, list1, deep):
#     for i in list1:
#         if i.isInteger():
#             sum1=sum1+(i.getInteger()*deep)
#         else:
#             sum1=sum1+recursion2(0, i.getList(), deep+1)
#     return sum1

# class Solution(object):
#     def depthSum(self, nestedList):
        
#         return recursion(nestedList)
        


def recursion(list1):
    return recursion2(0, list1, 1)
    
def recursion2(sum1, list1, deep):
    for i in list1:
        #print( sum1, i.isInteger(), deep)
        if isinstance(i,list):
            sum1=sum1+recursion2(0, i, deep+1)
        else:
            sum1=sum1+(i*deep)

            
    return sum1
        
        
        
def main():
    a=[[1,1],2,[1,1]]
    print( recursion(a))

if __name__ == "__main__":
    main()
        