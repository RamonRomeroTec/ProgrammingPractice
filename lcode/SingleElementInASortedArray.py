'''
ok
'''

class Solution:
    def singleNonDuplicate(self, nums):
        try:
            for  i in range(0,len(nums), 2):
                if nums[i]!=nums[i+1]:
                    if nums[i+1]==nums[i+2]:
                        return nums[i]
                    else:
                        return nums[i+1]
        except Exception as e:
            return nums[-1]



        # write your code here
if __name__ == '__main__':
    a=[1,1,2,2,3,4,4,8,8]
    s=Solution()
    print (s.singleNonDuplicate(a))
