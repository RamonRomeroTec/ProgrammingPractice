# Voltear Horizontalmente una imagen e invertirla
# los indices aseguran el cambio de valor en las referencias
# Uso de comprension de listas, considerar operaciones contantes en la modificacion

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i]=A[i][::-1]
            A[i] = [1-x for x in A[i]]
            
        return A