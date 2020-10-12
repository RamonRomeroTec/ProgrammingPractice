class Solution:
    def findJudge(self, N: int, trust):
        if N==1 and not trust:
            return 1

        # juez nobody 
        d={}
        d2={}
        for pair in trust:
            fr, to = pair
            if fr not in d:
                d[fr]=[to]
            else:
                d[fr].append(to)
                
            if to not in d2:
                d2[to]=1
            else:
                d2[to]+=1
                
        allpossible = { x for x in range(1, N+1)}
        possible = allpossible-set(d.keys())
        c=0
        j=-1
        for i in possible:
            if i in d2 and d2[i]==N-1:
                c+=1
                j=i
                if c>1:
                    return -1
        return j
            
        