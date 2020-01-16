# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(root, "")]
        val=[]
        while stack:
            x = stack.pop()
            node, bin_num = x[0], x[1]
            if node:
                if not node.left and not node.right:
                    #print(bin_num+str(node.val))
                    val.append(int(bin_num+str(node.val), 2))
                else:
                    if node.right:
                        stack.append( (node.right, bin_num+str(node.val)) )
                    if node.left:
                        stack.append( (node.left, bin_num+str(node.val)))
        #print(val)
        return sum(val)


