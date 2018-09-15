class Solution:
    """
    ok
    @param words: a list of string
    @return: a boolean

    '''
    [
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
00 00
01 10
03
    '''
    """
    def validWordSquare(self, words):
        for i in range (0, len(words)):
            for j in range(0, len(words[i])):
                if words[i][j]!=words[j][i]:
                    return False
        return True
