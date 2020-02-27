class Solution(object):
    def findSpecialInteger(self, arr):
        if len(arr)==1:
            return arr[0]
        c=1
        i=0
        while i<len(arr)-1:
            j=i+len(arr)//4
            if arr[i]!=arr[j]:
                h=i+1
                while arr[i]==arr[h]:
                    h+=1
                i=h
            else:
                return arr[i]



        