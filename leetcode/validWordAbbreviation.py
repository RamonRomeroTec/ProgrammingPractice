import re
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        l=re.findall(r'[A-Za-z]|[0-9]+', abbr)
        index=0
        try:
            for e in l:
                if e.isalpha():
                    if e != word[index]:
                        return False
                    index+=1
                else:
                    if e.lstrip("0") != e:
                        return False
                    index+=int(e)
        except:
            return False
        if index!=len(word):
            return False
        return True