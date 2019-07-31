# char and ord for initialization of an dictionary, ascii is only [0-25] inclusive 

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        d={}
        
        for i in range(0, 26):
            d[chr(ord('a')+i)]=widths[i]
        counter=0
        lines = 1
        for c in S:
            counter=counter+d[c]
            if counter>100:
                lines+=1
                counter=d[c]
        return [lines, counter]
                
                
            
        