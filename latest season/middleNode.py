'''

Note: race to find middle, double speed

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        i1 = head
        i2 = head
        while(i2 != None):
            i2 = i2.next
            if i2 == None:
                break
            i1 = i1.next
            i2 = i2.next
        return i1
        """
        :type head: ListNode
        :rtype: ListNode
        """
