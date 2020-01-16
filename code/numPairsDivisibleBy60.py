class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d={}
        for i in time:
            if i%60 in d:
                d[i%60]+=1
            else:
                d[i%60]=1
        visited=set()
        s=0
        for k,v in d.items():
            target = 60-k
            if target == 30 or target == 60:
                if d[k]>1:
                    s+=((v-1)*(v))//2
            else:
                if k not in visited:
                    if target in d:
                        s+=(v*d[target])
                        visited.add(target)
        return s
        