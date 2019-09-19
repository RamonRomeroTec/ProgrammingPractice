class Solution(object):
    def letterCombinations(self, digits):
        if digits=="":
            return []

        d={'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'],
           '6':['m','n','o'], '7':['p','q','r', 's'], '8':['t','u','v'], '9':['w','x','y', 'z'] }
        ans = ['']
        for di in digits:
            parcial = []
            for comb in ans:
                for l in d[di]:
                    parcial.append(comb+l)
            ans = parcial

        return ans