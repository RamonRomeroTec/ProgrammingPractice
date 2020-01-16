class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        t=0
        d=set()
        index=0
        while(index+K<=len(S)):
            if len(d)==K: #full w
                t+=1
                d.remove(S[index])
                try:
                    if S[index+K] in d:
                        index=index+K+1
                        d=set()
                    else:
                        d.add(S[index+K])
                        index+=1
                except:
                    return t
            else:
                for i in range(index,index+K):
                    if S[i] in d:
                        index=i+1
                        d=set()
                        break
                    else:
                        d.add(S[i])
        return t

#print(Solution().numKLenSubstrNoRepeats("havefunonleetcode", 5))
print(Solution().numKLenSubstrNoRepeats("aaabbaaaa", 2))

 