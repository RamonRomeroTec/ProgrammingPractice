# class Solution:
#     def sortArrayByParity(self, A: List[int]) -> List[int]:
#         pair = []
#         unpair =[]
#         for i in A:
#             if i%2 ==0:
#                 pair.append(i)


#             else:
#                 unpair.append(i)
#         return pair+unpair

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        return [ i for i in A if i%2== 0 ]+[ i for i in A if i%2!= 0 ]
    