class Solution:
    def balancedStringSplit(self, s: str) -> int:
        st=[]
        c=0
        for i in s:
            try:
                if ( i =='R' and st[-1]=='L') or ( i =='L' and st[-1]=='R') :
                    st.pop()
                else:
                    st.append(i)
            except:
                st.append(i)
            if not st:
                c+=1
        return c
        