from itertools import permutations 
class Solution:
    def largestTimeFromDigits(self, A):
        perm = permutations(A)
        strh=""
        strm=""
        maxh=-1
        maxm=-1
        for posible in list(perm):
            hours=(posible[0]*10)+(posible[1])
            mini=(posible[2]*10)+(posible[3])
            if hours<=23 and mini<=59:
                if hours > maxh:
                    maxh, maxm = hours, mini
                elif hours == maxh and mini>=maxm:
                    maxh, maxm = hours, mini
        if maxh==-1 or maxm==-1:
            return ""
        else:
            if maxh<10:
                strh='0'+str(maxh)
            else:
                strh=str(maxh)
            if maxm<10:
                strm='0'+str(maxm)
            else:
                strm=str(maxm)
            
            return strh+':'+strm
        