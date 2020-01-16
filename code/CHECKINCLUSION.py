# ---> ascii counter instead of hashing letters

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
       
        s2=list(s2)
        size_window=len(s1)
        s1=collections.Counter(s1)
        aux = collections.Counter(s2[0:size_window])
        
        if len(aux-s1)==0 and len(s1-aux)==0:
                return True

        
        for i in range(size_window, len(s2)):
            #print('>',i-size_window, i, aux)
            if aux[s2[i-size_window]] > 1:
                aux[s2[i-size_window]]=aux[s2[i-size_window]]-1
            else:
                del  aux[s2[i-size_window]]
            #print('>>',i-size_window, i, aux, 'a', s2[size_window] in aux)

            if s2[i] in aux:
                aux[s2[i]]+=1
            else:
                aux[s2[i]]=1
       
            if len(aux-s1)==0 and len(s1-aux)==0:
                #print (aux, s1)
                return True
            
        return False
        
        #"abcdxabcde"
#"abcdeabcdx"