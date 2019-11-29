class Solution(object):
    def frequencySort(self, s):
        a={}
        for c in s:
            if c not in a:
                a[c]=1
            else:
                a[c]+=1   
        return "".join([ x[0]*x[1] for x in (sorted(a.items(), key=lambda x:-x[1]))])