
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start=2
        end=x
        while True:
            mid1=(end-start)//2
            mid2=mid1+1

            if mid1*mid1<=x and x<=mid2*mid2:
                return mid1,mid2
            if mid1*mid1>x:
                end=mid1-1
            else:
                start=mid1+1
                
print(Solution().mySqrt(8))