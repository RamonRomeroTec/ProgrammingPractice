# AGARRAR MAXIMOS y MINIMOS GLOBALES BAJO EL MISMO PRINCIPIO POSICIONAL


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums.sort();
        #x=nums[0]*nums[1]*nums[-1]
        #y=nums[-3]*nums[-2]*nums[-1]


        #return max(x,y)
    
    
        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = -float('inf'), -float('inf'), -float('inf')
        
        for num in nums:
            if num < min1:
                min1 = num
                if min1 < min2:
                    min1, min2 = min2, min1
            
            if num > max1:
                max1 = num
                if max1 > max2:
                    max2, max1 = max1, max2
                if max2 > max3:
                    max3, max2 = max2, max3
        
        return max(min1*min2*max3, max1*max2*max3)