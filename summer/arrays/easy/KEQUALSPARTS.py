# DIVIDIR EL ARREGLO EN SUMAS IGUALES, PRIMERO VALIDARQUE SEA DIVISIBLE, 
# VER CUAL ES EL TAMAÑO DE CADA CUBETA E ITERAR 


class Solution(object):
    def canThreePartsEqualSum(self, A):
        full=sum(A)
        if full%3!=0:
            return False
        
        size=full//3
        s=0
        c=0
        for i in range(len(A)):
            s=s+A[i]
            if s==size:
                s=0
                c=c+1
            if c>3:
                return False
            elif c==3 and i==(len(A)-1):
                return True
        return False
            
        