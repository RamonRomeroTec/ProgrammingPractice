# Sorted -> binsearch
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        if target >= letters[-1]:
            return letters[0]
        left,right = 0,len(letters)
        while left < right:
            mid = left + (right - left)/2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return letters[right]