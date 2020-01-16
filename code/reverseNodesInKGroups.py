# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
#
'''
Given a linked list l, reverse its nodes k at a time and return the modified list.
k is a positive integer that is less than or equal to the length of l.
If the number of nodes in the linked list is not a multiple of k, then the nodes
that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.
'''

def reverseNodesInKGroups(l, k):
    a=[]
    while l!=None:
        a.append(l.value)
        l=l.next
    sizeb=int(len(a)/k)
    r=[]
    for i in range(0, sizeb):
        r=r+list(reversed(a[i*k:i*k+k]))
    return (r+a[len(r):])
