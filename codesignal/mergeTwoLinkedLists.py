# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
'''
Given two singly linked lists sorted in non-decreasing order,
your task is to merge them. In other words, return a singly linked list,
also sorted in non-decreasing order, that contains the elements
from both original lists.

'''
def mergeTwoLinkedLists(l1, l2):
    s=[]
    while 1:
        if l1== None and l2==None:
            break
        if l1== None or l2==None:


            if l2==None:
                s.append(l1.value)
                l1=l1.next
            elif l1==None:
                s.append(l2.value)
                l2=l2.next

            if l1== None and l2==None:
                break
        else:

            if  l1.value<l2.value:
                s.append(l1.value)
                l1=l1.next

            elif l1.value>=l2.value :
                s.append(l2.value)
                l2=l2.next

            if l1== None and l2==None:
                break


    return (s)
