'''
Note: Pointers over array(list) More than One

'''


class Solution(object):
    def diStringMatch(self, S):
        r=[ ]
        l=len(S)
        hi,low= l, 0
        for i in range(0,l):
            if S[i] == 'I':
                r.append(low)
                low=low+1  
            else:
                r.append(hi)

                hi=hi-1
                
        return r + [low]
            