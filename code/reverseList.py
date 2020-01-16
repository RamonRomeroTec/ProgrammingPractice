# MORE POINTERS

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        forward = head
        back=None
        while (forward):
            aux= forward.next
            forward.next= back
            back = forward
            forward=aux
        return back
            
        