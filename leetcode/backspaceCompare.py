class Solution(object):
    def backspaceCompare(self, S, T):
        s=[]
        for c in S:
            if c=='#':
                try:
                    s.pop()
                except:
                    pass
            else:
                s.append(c)
        a=[]
        for c in T:
            if c=='#':
                try:
                    a.pop()
                except:
                    pass
            else:
                a.append(c)
        return a==s
        
        