import re
class Solution(object):
    def mostCommonWord(self, p, banned):
        p = p.lower();
        list1=re.findall(r'\b\w+\b',p)
        banned = set(banned)
        maxi=0
        counter={}
        for w in list1:
            if w not in banned:
                if w not in counter:
                    counter[w]=1
                else:
                    counter[w]+=1
                if counter[w]>maxi:
                    maxi=counter[w]
                    key=w
        return key
                
                
        