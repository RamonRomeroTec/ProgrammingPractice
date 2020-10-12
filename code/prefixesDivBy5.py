class Solution:
    def prefixesDivBy5(self, A):
        s=0
        st=[]
        for index, v in enumerate(A):
            s= s | v<<len(A)-1-index
            st.append((s%5==0 or s%10==0))
        return st