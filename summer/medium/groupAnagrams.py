class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for s in strs:
            key= "".join(sorted(list(s)))
            if key not in d:
                d[key]=[s]
            else:
                d[key].append(s)
        return(d.values())
        