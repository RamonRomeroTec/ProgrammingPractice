class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        index = 0
        counter = 1
        while index < len(arr):
            if arr[index]==num:
                index+=1
            else:
                if counter == k:
                    return num
                counter+=1
            num+=1
        return arr[-1]+(k-counter+1)
        
