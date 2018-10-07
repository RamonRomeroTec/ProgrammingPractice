# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
'''
Given a singly linked list of integers l and a non-negative
integer n, move the last n list nodes to the beginning of the linked list.

'''
def rearrangeLastN(l, n):
    a=[]
    while l!=None:
        a.append(l.value)
        l=l.next
    f=len(a)
    a=a+a
    return(a[f-n:f-n+f])
