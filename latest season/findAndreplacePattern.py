'''
Note: two dictionaries or set to compare patterns

'''


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        r = []
        # szpat=len(pattern)
        for w in words:
            d = {}

            d2 = {}

            add = True
            # szword=len(w)

            for i in range(len(w)):
                # if szword!=szpat:
                #    add=False
                #    break

                if pattern[i] in d:
                    if w[i] not in d2 or d[pattern[i]] != w[i] or d2[w[i]] != pattern[i]:
                        add = False
                        break

                if w[i] in d2:
                    if pattern[i] not in d or d[pattern[i]] != w[i] or d2[w[i]] != pattern[i]:
                        add = False
                        break

                else:
                    d[pattern[i]] = w[i]
                    d2[w[i]] = pattern[i]

            if add == True:
                r.append(w)
        return r
