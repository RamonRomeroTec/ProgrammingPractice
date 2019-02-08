class Solution:
    """
    @param word: a string
    @return: return a boolean
    """
    def detectCapitalUse(self, word):
        if word[0]>='A'and word[0]<='Z':
            for i in range(1,len(word)-1):

                if (word[i]>='A'and word[i]<='Z' and word[i+1]>='a'and word[i+1]<='z') or (word[i]>='a'and word[i]<='z' and word[i+1]>='A'and word[i+1]<='Z'):
                    return False

        else:
             for i in range(1,len(word)):

                if word[i]>='A'and word[i]<='Z':
                    return False

        return True



        # write your code here
