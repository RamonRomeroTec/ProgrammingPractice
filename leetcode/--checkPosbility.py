def increase(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #[4,2,3]
        #[4,2,1]
        #
        # if asc by one diff
        if len(nums)==0 or len(nums)==1:
            return True
        c=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                l = nums[:i+1]
                r = nums[i+1:]
                print(l,r)
                if increase(l)==False :
                    return False
                elif increase(r)==False:
                    return False
                elif increase(l[-2:-1]+r[:2])==True:
                    return True
                elif increase(l[-2:]+r[1:2])==True:
                    return True
                else:
                    return False
                
            
            
                    
        return True
            