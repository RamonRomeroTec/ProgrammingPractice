# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tail(self, t, a):
        if t:
            a.append(str(t.val))
            if not t.left and not t.right:
                pass
            elif t.left and  not t.right:
                a.append('(')
                self.tail(t.left, a)
                a.append(')')
            elif not t.left and  t.right:
                a.append('()(')
                self.tail(t.right, a)
                a.append(')')

            else:
                a.append('(')
                self.tail(t.left, a)
                a.append(')(')
                self.tail(t.right, a)
                a.append(')')


            
        
    def tree2str(self, t):
        a=[]
        self.tail(t, a)
        s="".join(a)
        return (s)
        
        

        
        