class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k==0:
            if 0 in nums:
                return False
            return True
        a = []
        for i, e in enumerate(nums):
            if e == 1:
                a.append(i)
        for i in range(len(a)-1):
            for j in range(i+1, len(a)):
                if a[j]-a[i]-1 < k:
                    return False
        return True
        