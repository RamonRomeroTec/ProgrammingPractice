class Solution(object):
    def reverseOnlyLetters(self, s):
        a ,b = 0,len(s)-1
        s=list(s)
        while a<b:
            if s[a].isalpha() and s[b].isalpha():
                s[a], s[b] = s[b], s[a]
                a+=1
                b-=1
            elif s[a].isalpha() and not s[b].isalpha():
                b-=1
            elif not s[a].isalpha() and s[b].isalpha():
                a+=1
            elif not s[a].isalpha() and not s[b].isalpha():
                a+=1
                b-=1
        return "".join(s)