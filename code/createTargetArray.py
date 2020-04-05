class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in range(len(index)):
            target=target[:index[i]]+[nums[i]]+target[index[i]:]
        return target
            
        