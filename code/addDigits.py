#imperative is faster


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = sum(list(map(int,list(str(num)))))
        #print(l)
        if l>=10:
            return self.addDigits(l)
        else:
            return l
        