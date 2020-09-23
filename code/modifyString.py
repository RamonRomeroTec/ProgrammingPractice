class Solution:
    def modifyString(self, s: str) -> str:
        if len(s)==1:
            if s[0]=='?':
                return 'a'
            else:
                return s
        d='abc'
        di=0
        s=list(s)
        for i, l in enumerate(s):
            if l == '?':
                if i == 0:
                    while d[di%3]==s[i+1]:
                        di+=1
                    s[i]=d[di%3]
                elif i == len(s)-1:
                    while d[di%3]==s[i-1] :
                        di+=1
                    s[i]=d[di%3]
                else:
                    while d[di%3]==s[i+1] or d[di%3]==s[i-1]:
                        di+=1
                    s[i]=d[di%3]
        return "".join(s)