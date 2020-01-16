from collections import Counter

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        r=[]
        
        d1 = Counter(arr1)
        keys = set(arr2) 
        diff = set(d1.keys())-keys
        for k in arr2:
            if k in d1:
                r+= [k]*d1[k]
        for last in sorted(diff) :
            r+= d1[last]*[last]
        return r
        