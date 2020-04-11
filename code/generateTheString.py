class Solution:
    def generateTheString(self, n: int) -> str:
        if n==1:
            return 'a'
        if n%2==0:
            l=n-1
            return ("a"*l) + 'b'
        else:
            l=n-2
            return ("a"*l) + 'b' + 'c'
            
            
        