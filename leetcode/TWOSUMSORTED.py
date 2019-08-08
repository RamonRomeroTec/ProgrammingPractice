# CUANDO ESTA ORDENADO ES ALGUNA cosa DE POINTERS PARALELOS
# 

from collections import defaultdict
class Solution(object):
    def twoSum(self, numbers, target):
        # d=defaultdict(list)
        # for i in range(len(numbers)):
        #     d[numbers[i]].append(i)
        #     if numbers[i]>target:
        #         break
        # for k,v in d.items():
        #     print(target-k,d[target-k])
        #     if target-k in d and len(d[target-k])!=0:
        #         return sorted([d[target-k].pop()+1,v.pop()+1 ])

        start, end = 0 , len(numbers)-1

            
        while True:
            if numbers[start]+numbers[end]>target:
                end-=1
            elif numbers[start]+numbers[end]<target:
                start+=1
            else:
                return[start+1, end+1]
            
        
            
                
            
