class Solution:
    def makeGood(self, s: str) -> str:
        ans=[]
        for i in s:
            if not ans:
                ans.append(i)
            else:
                if i.isupper() and ans[-1].islower() and ans[-1].upper() == i:
                    ans.pop()
                elif i.islower() and ans[-1].isupper() and ans[-1].lower() == i:
                    ans.pop()
                else:
                    ans.append(i)
        return("".join(ans))
            
        