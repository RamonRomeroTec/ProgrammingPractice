from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        c=Counter(s)
        order_x=sorted(c.keys())
        br=set(c.keys())
        s=[]
        while True:
            for i in range(len(order_x)):
                if c[order_x[i]]>0:
                    s.append(order_x[i])
                    c[order_x[i]]-=1
                else:
                    if order_x[i] in br:
                        br.remove(order_x[i])
            for i in range(len(order_x)-1,-1,-1):
                if c[order_x[i]]>0:
                    s.append(order_x[i])
                    c[order_x[i]]-=1
                else:
                    if order_x[i] in br:
                        br.remove(order_x[i])
            if not br:
                break
        return "".join(s)