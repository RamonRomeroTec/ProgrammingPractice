class Solution(object):
    def freqAlphabets(self, s):
        d={'1':'a', '2':'b', '3':'c', '4':'d', '5':'e',
          '6':'f', '7':'g', '8':'h', '9':'i',
           '10#':'j', '11#':'k', '12#':'l',
           '13#':'m', '14#':'n', '15#':'o', '16#':'p',
           '17#':'q', '18#':'r','19#':'s', '20#':'t',
           '21#':'u', '22#':'v', '23#':'w', '24#':'x',
           '25#':'y', '26#':'z'}
        i=0
        ns=[]
        while i<len(s):
            p=i+2
            try:
                if s[p]=='#':
                    ns.append(d[s[i:p+1]])
                    i=p+1
                else:
                    ns.append(d[s[i]])
                    i+=1
            except:
                ns.append(d[s[i]])
                i+=1
        return "".join(ns)
            