# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current = head
        if not current:
            return False
        
        runner = current.next
        if runner == None:
            return False
        
        while runner:
            if runner.next:
                runner = runner.next
            else:
                return False
            if runner.next:
                runner = runner.next
            else:
                return False
            if runner == current:
                return True
            current=current.next
            
        return False