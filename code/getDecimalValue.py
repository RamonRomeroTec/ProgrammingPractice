class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=[]
        while head:
            s.append(head.val)
            head=head.next
        c=0    
        for i in range(len(s)):
            c+=(s[i]*(2**(len(s)-i-1)))  
        return c
