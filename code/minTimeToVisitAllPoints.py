class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if (len(points)==1):
            return 0
        s=0
        for i in range(len(points)-1):
            origin = points[i]
            destination = points[i+1]
            x1, y1 = origin[0] , origin[1]
            x2, y2 = destination[0] , destination[1]
            partial=0
            while True:
                if x1 == x2 :
                    s+=(partial+abs(y1-y2))
                    break
                elif x1<x2:#right
                    right=True
                else: # left
                    right=False   
                if y1 == y2 :
                    s+=(partial+abs(x1-x2))
                    break
                elif y1<y2:#up
                    up=True
                else: # down
                    up=False
                    
                if right:
                    if up:
                        x1+=1
                        y1+=1
                    else:
                        x1+=1
                        y1-=1
                else:
                    if up:
                        x1-=1
                        y1+=1
                    else:
                        x1-=1
                        y1-=1
                partial+=1
        return s


