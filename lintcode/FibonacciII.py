
"""

------------>#exectime 

@param n: an integer
@return: return a string

a = [[1, 0], [0, 1]]
>>> b = [[4, 1], [2, 2]]
>>> np.matmul(a, b)
array([[4, 1],
       [2, 2]])


import numpy.matlib
import numpy as np

a = [[1,1],[1,0]]
np.matmul(a, a)

import numpy.matlib
import numpy as np

a = [[1,1],[1,0]]
np.matmul(a, a)

"""



class Solution:

    def fib(self, n):
        fib=[]
        fib.append(0)
        fib.append(1)
        if n==0:
            return 0
        if n==1:
            return 1

        for i in range(0,n-1):
            fib.append(fib[i]+fib[i+1])
        return fib[-1]





    def lastFourDigitsOfFn(self, n):
        s=Solution()
        o=str(s.fib(n))
        if len(o)>4:
            return o[len(o)-4::]
        return o
        # write your code here




if __name__ == '__main__':
    t=9
    s=Solution()
    print (s.lastFourDigitsOfFn(t))
