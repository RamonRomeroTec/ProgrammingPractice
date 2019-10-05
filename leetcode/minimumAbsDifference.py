class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        mini=float('+inf')
        pairs=[]
        i=0
        while(i<len(arr)-1):
            j=i+1
            diff=abs(arr[i]-arr[j])
            if diff<mini:
                pairs=[[arr[i], arr[j]]]
                mini=diff
            elif diff==mini:
                pairs.append([arr[i], arr[j]])
            i+=1
        return(pairs)
    