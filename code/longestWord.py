class Solution(object):
    def longestWord(self, words):
        words=sorted(words, key=lambda x:(len(x), x))
        d={}
        for w in words:
            if w[:-1] not in d :
                d[w[:-1]]=[w]
            else:
                d[w[:-1]].append(w)
        s=[""]
        lw=[]
        while s:
            n=d[s.pop()]
            for subs in n:
                if subs not in d:
                    lw.append(subs)
                else:
                    s.append(subs)
        return sorted(lw, key=lambda x: ((-len(x), x)))[0]

            
        