from collections import deque

class Solution(object):
    def sumEvenGrandparent(self, root):
        q=deque([root])
        counter=0
        while q:
            current=q.popleft()
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            if current.val%2==0:
                if current.left:
                    if current.left.left:
                        counter+=current.left.left.val
                    if current.left.right:
                        counter+=current.left.right.val
                if current.right:
                    if current.right.right:
                        counter+=current.right.right.val
                    if current.right.left:
                        counter+=current.right.left.val
        return counter