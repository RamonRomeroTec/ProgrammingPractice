class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        arr1, arr2, arr3 = set(arr1), set(arr2), set(arr3)
        return list(sorted(arr1&arr2&arr3))
                
        