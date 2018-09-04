class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """
    def findTheDifference(self, s, t):
        '''
        l1=set()
        l2=set()
        for i in s:
            l1.add(i)
        for i in t:
            l2.add(i)
        a=None
        for first_item in (l2-l1):
            a=first_item
            break
        print(a)
        '''
        l1=[]
        l2=[]
        for i in s:
            l1.append(i)
        for i in t:
            l2.append(i)
        l1.sort()
        l2.sort()
        try:
            
            for i in range(0,len(t)):
                if l1[i]!=l2[i]:
                    return l2[i]
        except Exception as e:
            return l2[-1]

            

            


if __name__ == "__main__":

    t="abc"
    q="abcd"

    s=Solution()

    print(str(s.findTheDifference(t,q)))



