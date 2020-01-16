from collections import Counter
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=0
        b=len(s)-1
        c=0
        s1=False
        s2=False
        
        while a<b:
            aj=s[a]
            ax=s[b]
            if s[a] != s[b]:
                
                c+=1
                if c>1:
                    return False
                if s[a+1]==s[b]:
                    help1=a+1
                    help2=b
                    while help1<help2:
                        if s[help1] != s[help2]:
                            s1=False
                            break
                        else:
                            help1+=1
                            help2-=1
                        s1=True

            
                if s[a]==s[b-1]:
                    help1=a
                    help2=b-1
                    while help1<help2:
                        if s[help1] != s[help2]:
                            s2=False
                            break
                        else:
                            help1+=1
                            help2-=1
                        s2=True
                if s1 or s2:
                    return True
            a+=1
            b-=1
        return True
                    
            
            
                
            
print(Solution().validPalindrome(list("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")))
        