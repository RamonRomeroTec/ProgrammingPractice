'''

eval

'''

from collections import Counter

class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: the lowest ASCII sum of deleted characters to make two strings equal
    a="delete"
    b="leet"

    """
    def minimumDeleteSum(self, s1, s2):


        c = Counter(s1)
        d = Counter(s2)
        s=0


        #print (d-c)
        #print (c-d)
        #print((c)+(d))
        r= set(s1) & set(s2)

        l=(c+d)
        for i in l:
            if i not in r:
                s=s+(ord(i)*l[i])
            else:
                s=s+(ord(i)*(l[i]-2))
            #print(i,s)

            #print(i,s)


        return s

        #print(c)d1e2

        # Write your code here
if __name__ == '__main__':
    a="vwojt"
    b="saqhgdrarwntji"


    s=Solution()
    print(s.minimumDeleteSum(a,b))

    d="vosaqhgdrarni"
    s=0
    for i in d:
        s=s+ord(i)
    print (s)
