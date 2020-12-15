class Solution:
    def maxWidthOfVerticalArea(self, points):
        a = sorted(points, key= lambda x: x[0])
        d=0
        for i in range(len(a)-1):
            d=max(d, (a[i+1][0]-a[i][0]))    
        return d
            