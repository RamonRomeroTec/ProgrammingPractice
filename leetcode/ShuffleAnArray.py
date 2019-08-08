class Solution:
    start=[]
    aux=[]


    def __init__(self, nums):
        self.start=nums
        self.aux=self.start.copy()



        """
        :type nums: List[int]
        """

    def reset(self):
        self.start=self.aux.copy()
        return self.start
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """


    def shuffle(self):
        random.shuffle(self.start)
        return (self.start)

        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
