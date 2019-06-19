# find -1, index try

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s=set()
        for st in emails:
            st=st.split('@')
            a=st[0]
            b=st[1]
            a=a.replace('.','')
            if a.find('+') != -1:
                a=a[:a.find('+')]

            s.add(a+'@'+b)
        return len(s)
            
                
        