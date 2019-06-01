#EHEN LEADING WITH STRING NORMALIZE TO LOWER OR UPPER, single if lsist comprehension
from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A=Counter(A.split(' ')+B.split(' '))
        
        return  [ k for k,v in A.items() if v ==1 ]
    
   

        