class Solution:
    def reformatNumber(self, number: str) -> str:
        a=""
        for i in number:
            if i.isdigit():
                a+=i
        sz=len(a)
        ans=""
        c=0
        for i in range(sz):
            ans+=a[i]
            c+=1
            if c!=0 and c%3==0 and i!= (sz-1) :
                ans+='-'
        ans=ans.split('-')
        ev = ans[-1]
        if len(ev)==1:
            ans[-2]=ans[-2]+ans[-1]
            l=ans[-2][:2]
            r=ans[-2][2:]
            ans[-2]=l
            ans=ans[:-1]
            ans.append(r)
        return "-".join(ans)
            