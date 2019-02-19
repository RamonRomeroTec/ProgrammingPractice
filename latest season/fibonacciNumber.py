'''

Note: iterative or recursion may be correct approach

'''


class Solution(object):
    '''
    def fib(self, N):
        if N==0:
            return 0
        elif N==1:
            return 1
        else:
            return self.fib(N-1) + self.fib(N-2)
    '''

    def fib(self, N):
        a = [0, 1]
        if N == 0:
            return a[0]
        elif N == 1:
            return a[1]
        else:
            for i in range(2, N+1):
                a.append(a[i-1]+a[i-2])
            return a[N]
