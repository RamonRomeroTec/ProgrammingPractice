class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        s=list(format(N, 'b'))
        #print(s)
        for i in range(len(s)):
            if s[i]=='1':
                s[i]='0'
            else:
                s[i]='1'
        return int("".join(s), 2)
                
                
        