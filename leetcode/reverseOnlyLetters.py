class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        a=0
        b=len(S)-1
        s=list(map(str, S))
        
        while b>=a:
            if s[a].isalpha() and s[b].isalpha(): 
                s[a], s[b] =s[b], s[a]
                b-=1
                a+=1
            else:
                while a<(len(S)//2)+1:
                    if s[a].isalpha():
                        break
                    else:
                        a+=1
                while b>(len(S)//2)-1:
                    if s[b].isalpha():
                        break
                    else:
                        b-=1
            
                        
        return "".join(s)

        
print(Solution().reverseOnlyLetters("z<*zj"))