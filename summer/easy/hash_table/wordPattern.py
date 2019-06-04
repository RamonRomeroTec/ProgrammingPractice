#para garantizar bijection relationship, es necesario 2 dict

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str= str.split(" ")
        d1={}
        d2={}
        if len(pattern)!=len(str):
            return False
        
        for i in range(len(str)):
            try:
                if str[i] not in d1 and pattern[i] not in d2 :
                    d1[str[i]] = pattern[i]
                    d2[pattern[i]] = str[i]
                else:
                    try:
                        if d1[str[i]] != pattern[i] or d2[pattern[i]]!= str[i]:
                            return False
                    except:
                        return False
            except:
                pass
        return True
                
            
            
        