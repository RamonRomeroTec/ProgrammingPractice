# USE AN STACK TO EVALUATE THE CHANGES


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        memo = []
        for v in (ops):
            if v == '+':
                memo.append(memo[-1]+memo[-2])
            elif v == 'D':
                memo.append((memo[-1])*2)
            elif v == 'C':
                memo.pop()
            else:
                memo.append(int(v))
                
        return sum(memo)
        