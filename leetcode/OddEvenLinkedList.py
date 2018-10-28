# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def quick(node):
    counter=1
    i=[]
    p=[]
    while node:
        if counter%2:
            p.append(node)
        else:
            i.append(node)
        node=node.next
        counter=counter+1

    return p+i

def listtolinked(arr):
    if len(arr)==0:
        return []
    if len(arr)>1:
        for i in range(len(arr)-1):
            arr[i].next=arr[i+1]
        arr[-1].next=None
        return arr[0]
    else:
        arr[0].next=None
        return arr[0]





class Solution:
    def oddEvenList(self, head):
        a=quick(head)
        return listtolinked(a)
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
