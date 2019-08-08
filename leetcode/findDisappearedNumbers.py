# es posible usar rangos para la generacion de iterables, si usar comprenshion de listas


class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        compare = set(range(1,len(nums)+1))
        return compare-set(nums)
        
      