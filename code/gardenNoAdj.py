class Solution:
    def gardenNoAdj(self, N, paths):
        av={1,2,3,4}
        s={x:{'f':None, 'p':[]} for x in range(1, N+1)}
        for x in paths:
            o,d = x[0],x[1]
            s[o]['p'].append(d)
            s[d]['p'].append(o)
        for garden in s.keys():
            as1= av-{s[x]['f'] for x in s[garden]['p']}
            for e in as1:
                s[garden]['f']=e
                break
        return( [s[x]['f'] for x in range(1,N+1) ])
        