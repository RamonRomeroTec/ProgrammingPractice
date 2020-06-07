class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        l = sentence.split(" ")
        for i,w in enumerate(l):
            if searchWord==w[:len(searchWord)]:
                return i+1
        else:
            return -1
        