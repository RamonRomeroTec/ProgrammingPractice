class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels=set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        #S=list(map(list,(S.split(" "))))
        S=S.strip("\"").split(" ")
        print('S', S)
        
        for i in range(len(S)):
            if S[i][0] not in vowels:
                S[i]+=S[i][0]
                S[i]=S[i][1:]
            
            S[i]+="ma"+("a"*(i+1))
        
        return " ".join(S)
        