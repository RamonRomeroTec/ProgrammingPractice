# COMPRENSION DE LISTAS > CONCATENACION

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s=set()
        for word in words:
            nw=[]
            for letter in word:
                i = ord(letter)-ord('a')
                nw.append(d[i])
            s.add("".join(nw))
        return len(s)
                
        