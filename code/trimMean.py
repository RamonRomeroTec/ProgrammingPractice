class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr = sorted(arr)
        percent = int(len(arr)*.05)
        return sum(arr[percent:len(arr)-percent])/(len(arr)-(2*percent))
        