class Solution(object):
    def reverseOnlyLetters(self, s):
        if len(s)<2:
            return s
        end=len(s)-1
        begin = 0
        s=list(map(str, s))
        while (begin <= end):
            if s[begin].isalpha() and s[end].isalpha():
                s[begin],s[end] = s[end], s[begin]
                begin+=1
                end-=1
            while not s[begin].isalpha() and begin<len(s)-1:
                begin+=1
                if s[begin].isalpha():
                    break
            while not s[end].isalpha() and end>=0:
                end-=1
                if s[end].isalpha():
                    break
        return "".join(s)
            
        
            
            
            
            
            
            
            
        