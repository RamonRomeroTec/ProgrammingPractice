class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        i=2
        while i <= num:
            i=i*2
        return i-1-num
            
     