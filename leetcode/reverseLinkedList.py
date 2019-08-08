# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseListi(head):
    previous=None
    while head!=None:
        n=head.next
        head.next=previous
        previous=head
        head=n


    return previous


class Solution:
    def reverseList(self, head):
        return reverseListi(head)
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
