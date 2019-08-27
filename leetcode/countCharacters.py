class Solution(object):
    def countCharacters(self, words, chars):
        aux = collections.Counter(chars)
        ok=0
        ans=[]
        for word in words:
            c = dict(aux)
            i=0
            while i<len(word):
                if word[i] not in c:
                    break
                else:
                    c[word[i]]=c[word[i]]-1
                    if c[word[i]]==0:
                        del c[word[i]]
                i+=1
            if i==len(word):
                ans.append(word)
        return len("".join(ans))
                    
                