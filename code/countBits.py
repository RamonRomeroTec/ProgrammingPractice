class Solution:
    def countBits(self, num):
        a=[]
        for i in range(num+1):
            a.append(format(i, 'b').count('1'))
        return a
            
        