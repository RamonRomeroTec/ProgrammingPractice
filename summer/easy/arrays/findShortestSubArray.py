# IF NOT ORDERED DEFAULT DICT


from collections import Counter, defaultdict
class Solution(object):
    def findShortestSubArray(self, nums):
        s=Counter(nums)
        indexer=defaultdict(list)
        maxi=max(v for v in s.values())
        for i in range(len(nums)):
            indexer[nums[i]].append(i)
        
        mini=len(nums)
        for k,v in indexer.items():
            if len(v)==maxi:
                diff = v[-1]-v[0]+1
                if diff< mini:
                    mini=diff
        
        return mini
            
            
        """
        :type nums: List[int]
        :rtype: int
        """
# from collections import Counter
# class Solution(object):
#     def findShortestSubArray(self, nums):
#         s=Counter(nums)
#         maxi=max(v for v in s.values())
#         maxs=set()
#         for k,v in s.items():
#             if v==maxi:
#                 maxs.add(k)
#         totlen=len(nums)
#         mini=len(nums)
#         for i in maxs:
#             st=nums.index(i)
#             end=totlen-nums[::-1].index(i)
#             diff=end-st
#             if diff< mini:
#                 mini=diff

#         return mini
            
        