'''
Note: use, sets as collection using set and any

'''


class Solution(object):
    def findWords(self, words):
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        a = set(r1)
        b = set(r2)
        c = set(r3)
        r = []
        for w in words:
            if len(a & set(w)) >= 1 and len(b & set(w)) == 0 and len(c & set(w)) == 0:
                r.append(w)
            elif len(b & set(w)) >= 1 and len(c & set(w)) == 0 and len(a & set(w)) == 0:
                r.append(w)
            elif len(c & set(w)) >= 1 and len(a & set(w)) == 0 and len(b & set(w)) == 0:
                r.append(w)
        return r
        """
        :type words: List[str]
        :rtype: List[str]
        class Solution(object):
        def findWords(self, words):
        rs = map(set,['qwertyuiop','asdfghjkl','zxcvbnm'])
        ans = []
        for word in words:
            wset = set(word.lower())
            if any(wset <= rset for rset in rs):
                ans.append(word)
        return ans
        """
