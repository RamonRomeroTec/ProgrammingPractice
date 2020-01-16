'''
Note: Sending all to a set will impply more time than iterate over the adding

'''


class Solution(object):
    def containsDuplicate(self, nums):
        '''
        a=set(nums)
        if len(a)!=len(nums):
            return True
        else:
            return False
        '''
        d=set()
        for i in nums:
            if i in d:
                return True
            else:
                d.add(i)
        return False
        
        