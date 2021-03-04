class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        s=0
        for k, v in c.items():
            if v == 1:
                s+=k
        return s
                