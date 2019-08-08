# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         s=set()
#         for number in nums:
#             if number not in s:
#                 s.add(number)
#             else:
#                 return True
#         return False
            
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)    