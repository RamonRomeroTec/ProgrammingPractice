"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

def rev(head, s):
    if head==None:
        return s

    s.append(head)
    head=head.next

    return rev(head,s)







def stacktoLL(s):
    if len(s)==0:
        return None
    else:
        s[-1].next=None
        if len(s)>1:
            for i in reversed(range(1,len(s))):
                s[i].next=s[i-1]
            s[0].next=None



        return s[-1]


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        s=[]
        r=rev(head, s)
        return stacktoLL(r)
