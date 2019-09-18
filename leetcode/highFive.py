class Solution(object):
    def highFive(self, items):
        d={}
        for pair in items:
            ln=pair[0]
            cal=pair[1]
            if ln not in d:
                d[ln]=[cal]
            else:
                d[ln].append(cal)
        l1=[]
        for iden in d.keys():
            top = sorted(d[iden])[::-1][0:5]
            l1.append([iden, sum(top)//5])
        return l1
        