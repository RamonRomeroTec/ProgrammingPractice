from collections import deque
class Solution:
    def sumOddLengthSubarrays(self, arr):
        q=[]
        s=0
        if len(arr)%2==0:# slide
            q=[deque(arr[:-1]),deque(arr[1:])]
            au=sum(arr)
            s+=au-arr[-1]
            s+=au-arr[0]
        else:
            q=[deque(arr[:])]
            s+=sum(arr)
        while q:
            current = q.pop()
            if len(current)>1:
                au2=sum(current)
                s+=au2-current[0]-current[-1]
                s+=au2-current[-2]-current[-1]
                s+=au2-current[0]-current[1]
                print(current)
                l1=current.copy()
                l1.pop()
                l1.pop()
                l2=current.copy()
                l2.pop()
                l2.popleft()
                l3=current.copy()
                l3.popleft()
                l3.popleft()
                q.append(l1)
                q.append(l2)
                q.append(l3)
        return s
                
                
print(Solution().sumOddLengthSubarrays([1,4,2,5,3]))