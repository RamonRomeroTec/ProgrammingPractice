def generateNext(s):
    if len(s)==1:
        return s+s
    ans=""
    p = 0
    q = 1
    times=1
    while q<len(s) and p<len(s):
        if s[p] == s[q]:
            times+=1
        else:
            ans = ans + str(times)+s[p]
            times=1
            p=q
            q=p+1
            continue
        q+=1
    ans = ans + str(times)+s[p]
    return ans


class Solution(object):
    def countAndSay(self, n):
        a=['1']
        for i in range(n-1):
            a.append(generateNext(a[-1]))
        return a[-1]
        