# USAR UNA HASH TABLE ES MEJOR QUE UN SORT

class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        arr = []
        for r in range(R):
            for c in range(C):
                man_dis=abs(r0-r)+abs(c0-c)
                arr.append( ((r,c), man_dis))
        
        return [ x[0] for x in sorted(arr,key=lambda x : x[1])]
    
        # d = collections.defaultdict(list)
        # for i in range(R):
        #     for j in range(C):
        #         d[abs(i-r0)+abs(j-c0)].append([i,j])
        # max_distance = max(d.keys())
        # out = []
        # for dis in range(max_distance+1):
        #     out.extend(d[dis])
        # return out
        