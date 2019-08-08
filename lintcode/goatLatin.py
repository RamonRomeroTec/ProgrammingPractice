class Solution:
    """
    @param S:
    @return: nothing
    """
    def  toGoatLatin(self, s):
        s=s.split(' ')
        vowels=set(['a','e','i','o', 'u', 'U', 'A', 'E', 'I', 'O'])
        ended=[]
        for i in range(0,len(s)):
            print(s[i])
            if s[i][0] in vowels:
                n=s[i]+'ma'
            else:
                n=s[i][1:]+s[i][0] +'ma'
            n=n+str((i+1)*'a')
            ended.append(n)



        return " ".join(ended)
        #
