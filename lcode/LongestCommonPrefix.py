class Solution:

    def index(self,strs):
        contin=True
        for i in range(0,len(strs[0])):
            for j in range(0,len(strs)-1):
                if i >= len(strs[j+1]):
                    return i
                if strs[j][i]!=strs[j+1][i]:
                    return i

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        else:

            s=Solution()
            i=s.index(strs)
            return strs[0][0:i]


if __name__ == '__main__':
    strs=["aaa","aa","aaa"]
    s=Solution()
    print(s.longestCommonPrefix(strs))
