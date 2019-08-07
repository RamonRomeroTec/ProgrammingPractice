
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0 or len(s)==1:
            return s
        s=list(map(str,list(s)))
        last = len(s)-1
        init = 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        while init <= last:
            if s[init] in vowels:
                while last >=init:
                    if s[last] in vowels:
                        s[init], s[last] = s[last], s[init]
                        last=last-1
                        break
                    else:
                    
                        last=last-1
                    
            init=init+1
        return "".join(s)
        