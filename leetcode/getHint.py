class Solution(object):
    def getHint(self, secret, guess):
        a={}
        b={}
        B=0
        for i, v in enumerate(secret):
            if v == guess[i]:
                B+=1
            else:
                if v not in a:
                    a[v]=1
                else:
                    a[v]+=1
                if guess[i] not in b:
                    b[guess[i]]=1
                else:
                    b[guess[i]]+=1
        s=0
        for k in set(a.keys())&set(b.keys()):
            s+=min(a[k],b[k])
        return str(B)+'A'+str(s)+'B'
            
        