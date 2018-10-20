"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

def evaluate(t1,t2):
    #si no existe devuelve el nodo
        if  t2 == None:
            return t1

        elif t1 == None:
            return t2
    #recursiva validacion

        elif t1 != None and t2 != None:
            t1.val=t1.val+t2.val
            t1.left=evaluate(t1.left,t2.left)
            t1.right=evaluate(t1.right,t2.right)

    #devuelve head
            return t1





class Solution:
    """
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """
    def mergeTrees(self, t1, t2):
        return evaluate(t1,t2)





        # Write your code here
