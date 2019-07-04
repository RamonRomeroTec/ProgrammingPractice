class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        a=[]
        for limit,letter in enumerate(S):
            izq=(S[limit::-1]).find(C)
            der=S[limit:].find(C)
            print(izq, der)
            if izq == -1:
                a.append(der)
            elif der == -1 :
                a.append(izq)
            else:
                a.append(min(izq,der))
        return a
        