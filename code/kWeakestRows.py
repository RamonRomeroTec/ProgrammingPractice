class Solution:
    def kWeakestRows(self, mat, k):
        a=[]
        for i,line in enumerate(mat):
            a.append((i, sum(line)))
        a=sorted(a, key=lambda x:x[1])
        return [a[i][0] for i in range(k)]
            