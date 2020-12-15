class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        it1= list1
        ar=[]
        c=0
        while it1:
            if c == a-1:
                ar.append(it1)
            if c == b+1:
                ar.append(it1)
            it1=it1.next
            c+=1            
        ar[0].next=list2
        it2=list2
        while it2.next:
            it2=it2.next
        it2.next =ar[1]
        return list1
        9