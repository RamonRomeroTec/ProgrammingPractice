'''
Note: List comprehension reduce el tiempo

'''

class Solution(object):
    '''
    def sortedSquares(self, A):
        n=[]
        for i in A:
            n.append(i**2)
        return sorted(n)
    '''
    def sortedSquares(self, A):

        return sorted([x*x for x in A])
      