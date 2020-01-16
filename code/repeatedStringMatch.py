class Solution(object):
    def repeatedStringMatch(self, A, B):
        N=A
        c=1
        while True:
            print(N)
            if B in N:
                return c
            else:
                N=N+A
            c+=1
        
print(Solution().repeatedStringMatch("abcabcabcabc","abac"))