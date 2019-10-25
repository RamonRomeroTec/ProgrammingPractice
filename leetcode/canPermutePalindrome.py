class Solution(object):
    def canPermutePalindrome(self, s):
        c=collections.Counter(s)
        size=len(s)
        if size%2==0:
            for v in c.values():
                if v%2!=0:
                    return False
            return True
        else:
            count=0
            for v in c.values():
                if v%2!=0:
                    count+=1
                if count>1:
                    return False
            return True