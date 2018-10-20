class Solution:
    """
    @param words: the given list of words
    @return: the number of different transformations among all words we have
    """
    def uniqueMorseRepresentations(self, words):
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        '''
        letras=[ chr(x) for x in range(ord('a'),ord('z')+1)]
        d={}
        for i in range(len(letras)):
            d[letras[i]]=morse[i]
        '''
        f=set()
        for i in words:
            a=""
            for l in i:
                a=a+morse[ord(l)-ord('a')]

            f.add(a)


        return len(f)

        # Write your code here
