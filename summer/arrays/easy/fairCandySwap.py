       
# CONSIDERAR CAMBIOS DE SIGNO EN OPERAACIONES DE RESTA, EL USO DEL SET
# REDUCE EL ACCESO

# class Solution(object):
#     def fairCandySwap(self, A, B):
#         auxA=sum(A)
#         auxB=sum(B)
#         important= abs(auxA-auxB)//2
#         B=set(B)
#         #print(important)
#         newA=None
#         if auxA>auxB:
#             newA=auxA-important
            
#         else:
#             newA=auxA+important
#         for i in A:
#                 X=(newA + i - auxA)
#                 if  X in B:
#                     return[i,X]
#                 #try:
#                 #    return [i, B[B.index(X)]]
#                 #except:
#                 #    pass
    


class Solution(object):
    def fairCandySwap(self, A, B):
      
        important= (sum(A)-sum(B))//2
        B=set(B)
        #print(important)
        for i in A:
            if i-important in B:
                return [i, i-important]