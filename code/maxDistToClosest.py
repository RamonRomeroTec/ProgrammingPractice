class Solution(object):
    def maxDistToClosest(self, seats):
        init=0
        c=0
        maxi=(c, (init, None))
        for i, e in enumerate(seats): 
            if e == 0:
                c+=1
            elif e==1:
                if c>maxi[0]:
                    maxi=(c, (init, i))
                init=i+1
                c=0
            if i==len(seats)-1:
                if c>maxi[0]:
                    maxi=(c, (init, i))
        if maxi[1][0] == 0:
            return 0
        elif maxi[1][1] == len(seats)-1:
            return len(seats)-1
        else:
            return ((maxi[1][1]-maxi[1][0])//2)+maxi[1][0]

print(Solution().maxDistToClosest([0,1]))
                                    
            
            
            
        