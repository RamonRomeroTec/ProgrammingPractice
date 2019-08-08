# REVERSING UNTIL HALF, 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        c=1
        p1 = head
        if not p1:
            return True
        
            
        p2 = p1.next
        c=c+1
        back = None
        
        while p2:
        #     REVERSE HERE
            aux = p1.next
            p1.next = back
            back = p1
            p1 = aux
            
            if p2.next:
                c=c+1
                p2=p2.next
            else:
                break
            if p2.next:
                c=c+1
                p2=p2.next
            else:
                break
        if c%2 != 0:
            p1 = p1.next
        while back:
            if back.val != p1.val:
                return False
            back = back.next
            p1 = p1.next
        return True
        