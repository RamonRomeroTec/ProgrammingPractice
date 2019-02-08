from collections import defaultdict

class Solution:
    def twoSum(self, ns, t):
            a=list(enumerate(ns))
            d = defaultdict(list)
            for i, v in a:
                d[v].append(i)


            for i in d:
                lf=t-i
                if lf in d:

                    j=d[lf]

                    if len(j)==1:
                        return [d[i][0],j[0]]
                    else:
                        return [d[i][0],j[1]]
