class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=max(candies)
        return [ True if x+extraCandies >= a else False for x in candies]
        