# RACE EXAMPLE

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        quick=head
        slow=head
        while (quick):
            print(quick.val, slow.val)
            quick=quick.next
            if quick != None:
                quick=quick.next
            else:
                break
            slow=slow.next
        return slow
        """
        :type head: ListNode
        :rtype: ListNode
        """
        