# iterative not listing
class Solution(object):
    def sumOfDigits(self, A):

        minimo = min(A)
        suma=0
        while minimo>0:
            suma+=(minimo%10)
            minimo//=10
        if suma%2 == 0:
            return 1
        else:
            return 0
        
        