class Solution(object):
    def isBoomerang(self, points):
        p1=points[0]
        p3=points[2]
        p2=points[1]
        if p1[0] == p2[0] and p2[0] == p3[0]:
            return False
        if p1[1] == p2[1] and p2[1] == p3[1]:
            return False
        if p1 == p3 and p2 != p3:
            p2, p3 = p3, p2
        try:
            slope=float(p3[1]-p1[1])/float(p3[0]-p1[0])
        except:
            return True
        b=p1[1]-slope*p1[0]
        return(not (slope*p2[0])+b == p2[1])
        
        
        