class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        sp=  set('aeiouAEIOU')
        fh=0
        sh=0
        for i in range(len(s)//2):
            if s[0+i] in sp:
                fh+=1
            if s[len(s)//2+i] in sp:
                sh+=1
        return fh==sh
                
            