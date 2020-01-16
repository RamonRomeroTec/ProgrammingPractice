# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def deeping(node, g):
    if node:
        if node.val in g:
            return deeping(node.next, g)
        else:
            return node.next
    return node
            

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        
        G = set(G)
        s=0
        start = head
        while start:
            if start.val in G:
                s=s+1
                start = deeping(start, G)
                
                    
            else:
                start=start.next
        return s
                
            