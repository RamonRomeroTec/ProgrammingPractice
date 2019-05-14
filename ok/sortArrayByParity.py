'''

Note: [-1]*len(A) to create dummy array, or none;
       var as pointers

'''


class Solution(object):
    def sortArrayByParityII(self, A):
        r = [-1]*len(A)
        i = 0
        j = 1
        for e in A:
            if e % 2 == 0:
                # print(i,r)
                r[i] = e
                i = i+2
            else:
                r[j] = e
                j = j+2
        return r
