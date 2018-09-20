from collections import Counter
class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """

    def numJewelsInStones(self, J, S):
        s=0

        c=Counter(S)
        p=set(J)
        for i in c:
            if i in p:
                s=s+c[i]

        return s
