# uso de colleccionde dentoro de la funcion, parece reducrie el tiempo de importacion local
# operadores unarios tambien parecen reducir el tiempo
# r'[operand]+=
# elements, operacion de itertool element permite la concatencacion de elementos existentes
# dentro de los contadores
# map & reduce, en especifico reduce como simplificacion de una lista, similar a sum/ avg

from collections import Counter
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        
        #r=collections.Counter(A[0])  
        r=Counter(A[0])  
        for i in range(len(A)):
            r&=Counter(A[i])      
        return(list(r.elements()))
            
            
            
            
        