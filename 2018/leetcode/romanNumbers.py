
class Solution:
    def romanToInt(self, s):
        d={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
               'IV':4, 'IX': 9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        n=0
        i=0
        while i<len(s):
            if i+1<len(s) and s[i]=='I' and s[i+1]=='V':
                n=n+d['IV']
                i=i+2

            elif i+1<len(s) and s[i]=='I' and s[i+1]=='X':
                n=n+d['IX']
                i=i+2




            elif i+1<len(s) and s[i]=='X' and s[i+1]=='L':
                n=n+d['XL']
                i=i+2
                
            elif i+1<len(s) and s[i]=='X' and s[i+1]=='C':
                n=n+d['XC']
                i=i+2

            elif i+1<len(s) and s[i]=='C' and s[i+1]=='D':
                n=n+d['CD']
                i=i+2

            elif i+1<len(s) and s[i]=='C' and s[i+1]=='M':
                n=n+d['CM']
                i=i+2
            else:
                n=n+d[s[i]]
                i=i+1
        return n
