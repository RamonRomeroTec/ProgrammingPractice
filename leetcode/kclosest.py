class Solution(object):
    def kClosest(self, points, K):
        d={}
        for p in points:
            euclidean = (((p[0]**2 )+(p[1]**2)))
            if euclidean in d:
                d[euclidean].append(p)
            else:
                d[euclidean]=[p]
        aux=[]  
        for k in sorted(d.keys()):
            for e in d[k]:
                if len(aux)==K:
                    return aux
                else:
                    aux.append(e)
            if len(aux)==K:
                    return aux
       