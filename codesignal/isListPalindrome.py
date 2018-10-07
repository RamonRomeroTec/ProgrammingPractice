# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    s=[]
    h=l
    while l != None:
        s.append(l.value)
        l=l.next

    while h!=None:
        if s.pop()!= h.value:
            return False
        h=h.next
    return True
