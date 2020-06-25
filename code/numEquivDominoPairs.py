
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        s={}
        for i in dominoes:
            if i[0]<i[1]:
                if (i[0],i[1]) in s:
                    s[(i[0],i[1])]+=1

                else:
                    s[(i[0],i[1])]=1
            else:
                if (i[1],i[0]) in s:
                    s[(i[1],i[0])]+=1

                else:
                    s[(i[1],i[0])]=1
        c=0
        for v in s.values():
            if v >= 2:
                c += ((v*(v-1))//2)
        return c
        