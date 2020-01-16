class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word = list(map(str, list(word)))
        
        if word[0].isupper():
            mayus=1
            minus=0
            
            for j in range(1, len(word)):
                if word[j].isupper():
                    mayus+=1
                else:
                    minus+=1
                #print(word[j].isupper,word[j],mayus, minus)
                if mayus > 1 and minus >0:
                    return False
                
            if mayus == len(word):
                return True
            if mayus == 1 and minus == len(word)-1:
                return True
                    
                
            
        else:
            for j in range(1,len(word)):
                if word[j].isupper():
                    return False
        return True