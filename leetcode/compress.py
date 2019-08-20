class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) >1:
            p = 0
            q = 1
            c = 1
            ans=[]
            while p < len(chars) and q< len(chars):
                if chars[p]==chars[q]:
                    c+=1
                else:
                    ans.append(chars[p])
                    if c>1:
                        map(ans.append, str(c))
                    c=1
                    p=q
                    q=p+1
                    continue
                q+=1
            ans.append(chars[-1])
            if c>1:
                map(ans.append, str(c))
            chars[:]=ans[:]
                
        