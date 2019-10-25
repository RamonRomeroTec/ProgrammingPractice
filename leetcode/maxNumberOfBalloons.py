class Solution(object):
    def maxNumberOfBalloons(self, text):
        d = collections.Counter(text)
        b={'b':1, 'a':1, 'l':2, 'o':2 , 'n':1}
        mini=float("+inf")
        for k, v in b.items():
            if k not in d:
                return 0
            else:
                mini=min(mini,d[k]//v)
        return mini
                
        