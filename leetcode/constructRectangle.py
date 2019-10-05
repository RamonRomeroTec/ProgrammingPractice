class Solution(object):
    def constructRectangle(self, area):
        l=int(math.sqrt(area))
        w=area/l
        while not l*w==area:
            l-=1
            w=area/l 
        if l>=w:
            return [l, w]
        else:
            return [w, l]
                
           