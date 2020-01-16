# Dada una lista, poner pares primero y postriormente los impares
# # Comprension y concatenacion de listas

class Solution:
    def sortArrayByParity(self, A):
        
        return [ i for i in A if i%2== 0 ]+[ i for i in A if i%2!= 0 ]
    