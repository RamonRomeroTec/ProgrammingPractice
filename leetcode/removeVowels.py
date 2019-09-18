class Solution(object):
    def removeVowels(self, S):
        v=set("aeiou")
        return "".join([x for x in S if x not in v])
        