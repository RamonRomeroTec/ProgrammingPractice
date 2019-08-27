class Solution(object):
    def findRestaurant(self, list1, list2):
        inter = set(list1)&set(list2)
        d1={}
        for i,v in enumerate(list1):
            d1[v]=i
        d2={}
        for i,v in enumerate(list2):
            d2[v]=i
        mini=10000 
        final={}
        for i in inter:
            loc = d2[i]+d1[i]
            if loc in final:
                final[loc].append(i)
            else:
                final[loc]=[i]
            if loc < mini:
                mini=loc
        return final[mini]