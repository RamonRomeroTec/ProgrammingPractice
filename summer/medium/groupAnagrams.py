from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d=defaultdict(list)
        for s in strs:
            aux = tuple(sorted(list(s)))
            d[aux].append(s)
        return(d.values())
        