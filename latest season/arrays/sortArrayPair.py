'''
Note: Probar Naive Solution 

'''
class Solution(object):
    def sortArrayByParity(self, A):
        pair=[]
        inpair=[]
        for i in A:
            if i%2==0:
                pair.append(i)
            else:
                inpair.append(i)
        return pair+inpair


        