class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        aux = [2,3,5]
        a=0
        while a < len(aux) and num > 0:
            #print(a,num)
            if num%aux[a] == 0:
                num = num // aux[a]
            else:
                a+=1
        if num == 1:
            return True
        return False
            
            
        