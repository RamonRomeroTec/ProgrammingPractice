# CONSIDERAR LISTAS NULAS E INIZIALIZACIONES POR DEFAULT EN NULO


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        r = head
        current = head
        if not current:
            return r
        runner = current.next

        while (runner):
            if runner.val == current.val:
                while runner and runner.val == current.val:
                    runner = runner.next
                current.next=runner
            current = current.next
            if not current:
                break
            runner = current.next
            
        
        return r
        