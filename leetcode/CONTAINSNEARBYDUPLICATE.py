
#   UTILIZAR EL INDICE ACTUAL DENTRO DE LA ITERACION DE LA LECTURA PARA COMPARAR
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=i
            else:
                if abs( d[nums[i]] - i) <= k:
                    return True
                else:
                    d[nums[i]]=i
                    
        return False

        # d=defaultdict(list)
        
        # """
        # :type nums: List[int]
        # :type k: int
        # :rtype: bool
        # """
        # for i,n in enumerate(nums):
        #     d[n].append(i)
        
        # for l in d.values():
        #     if len(l)>=2:
        #         for i in range(len(l)-1):
        #             for j in range(i+1,len(l)):
        #                 if abs(l[i]-l[j]) <= k :
        #                     return True
        # return False
      