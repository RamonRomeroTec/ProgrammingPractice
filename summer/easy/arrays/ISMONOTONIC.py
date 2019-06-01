# PARA VALIDAR SI UN AREGLE ES DESCENCIENTE O ASCENDIENTE BASTA CON COMPARAR
# EL PRIMERO Y EL ULTIMO DE LOS ARREGLOS

class Solution(object):
    def isMonotonic(self, A):
        if len(A)==1:
            return True
        elif len(A)==2 and A[0] == A[1]:
            return True
        else:
            ascending=None
            if A[0] > A[-1]:
                ascending=False
            else:
                ascending=True
                
           
            for j in range (len(A)-1):
                #print(ascending, A[i] , A[i+1])
                if ascending==True and A[j] > A[j+1]:
                    return False
                elif ascending==False and A[j] < A[j+1]:
                    return False
            return True
            
        
        
            
            
            
            
        """
        :type A: List[int]
        :rtype: bool
        """
        
# class Solution(object):
#     def isMonotonic(self, A):
#         if len(A)==1:
#             return True
#         elif len(A)==2 and A[0] == A[1]:
#             return True
#         else:
#             ascending=False
#             for i in range(len(A)-1):
#                 if A[i] > A[i+1]:
#                     ascending=False
#                     break
#                 elif A[i] < A[i+1]:
#                     ascending=True
#                     break
#             for j in range (i+1,len(A)-1):
#                 #print(ascending, A[i] , A[i+1])
#                 if ascending==True and A[j] > A[j+1]:
#                     return False
#                 elif ascending==False and A[j] < A[j+1]:
#                     return False
#             return True
            
        
        
            
            
            
            
#         """
#         :type A: List[int]
#         :rtype: bool
#         """
        