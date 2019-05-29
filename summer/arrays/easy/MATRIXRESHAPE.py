# given a 2d array, emulate reshape fuction, flatten an then split by index

class Solution(object):
    def matrixReshape(self, nums, r, c):
        flatten = [e for line in nums for e in line]
        size=len(flatten)
        if r*c != size:
            return nums
        return [ flatten[i:i+c] for i in range(0,size, c)]
        
        
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        