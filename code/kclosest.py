class Solution(object):
    def kClosest(self, points, K):
        return sorted([[p[0], p[1]] for p in points], key=lambda x:(x[0]**2+x[1]**2))[:K]
       