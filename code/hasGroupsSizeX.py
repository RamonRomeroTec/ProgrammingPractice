class Solution(object):
    def hasGroupsSizeX(self, deck):
        if len(deck)<=1:
            return False
        a={}
        for i in deck:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        maxi=max(a.values())
        primes=[2,3,5,7,11,13,	17,	19,	23,	29, 31, 37, 41, 43,	47,	53,	59,	61,	67,	71 ]
        for p in primes:
            if p>maxi:
                return False
            c=0
            for v in a.values():
                if v%p!=0:
                    break
                if c==len(a)-1:
                    return True
                c+=1
                    
            
        