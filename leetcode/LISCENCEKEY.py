'''
FOR PIECES IS QUICKER THAN 
'''
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S=list(S.replace("-", "").upper())
        ans=[]
        a=0
        upper = len(S)
        lower = len(S)-K
        if len(S)<=K:
            return "".join(S)
        
        while (lower>=0 ):
            ans.append("".join(S[lower:upper]))
            upper=lower
            lower = lower-K
            if lower<0 and upper>0:
                ans.append("".join(S[0:upper]))
                break
                
            
        return "-".join(ans[::-1])
            
        
            
        