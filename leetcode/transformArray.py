class Solution(object):
    def transformArray(self, arr):
        while True:
            state=[0 for x in range(len(arr))]        
            no=0
            for i in range(1, len(arr)-1):
                if arr[i]<arr[i+1] and arr[i]<arr[i-1]:
                    state[i]=1
                elif arr[i]>arr[i+1] and arr[i]>arr[i-1]:
                    state[i]=-1
                else:
                    no+=1

            for i in range(len(arr)):
                arr[i]+=state[i]
                
            if no==len(arr)-2:
                break

        return(arr)
                
        