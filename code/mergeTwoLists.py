# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and not l2:
            return l1
        elif l2 and not l1:
            return l2
        elif not l2 and not l1:
            return None
        else:
            p1 = l1
            p2 = l2
            selected = None
            if p1.val <= p2.val:
                selected = p1
                p1=p1.next
            else:
                selected = p2
                p2=p2.next
            head = selected  
            while (p2 and p1):
                if p1.val <= p2.val:
                    selected.next = p1
                    p1=p1.next
                else:
                    selected.next = p2
                    p2=p2.next
                
                    
                selected = selected.next
            if not p2:
                selected.next = p1
            else:
                selected.next = p2
            return head
                

                
        