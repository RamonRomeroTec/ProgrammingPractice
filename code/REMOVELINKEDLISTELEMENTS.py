# CHECK EDGE CASES FOR CONDITIONALS

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head
        if current == None:
            return head
        while (current and current.val == val):
            current = current.next
        if current == None:
            return None
    
        head = current
        p1 = None
        if current.next:
            p1 = current.next
        else:
            return head
        while current and p1:
            if p1.val == val:
                while p1 and p1.val == val:
                    p1=p1.next
                current.next = p1
                
            current = current.next
            if not current:
                break
            p1 = current.next
        
        
        
            
            
        return head
            
        