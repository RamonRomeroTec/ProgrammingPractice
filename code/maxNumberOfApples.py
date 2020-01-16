class Solution(object):
    def maxNumberOfApples(self, arr):
        arr.sort()
        s=0
        c=0
        for w in arr:
            s+=w
            if s>5000:
                break
            c+=1
        return c
        