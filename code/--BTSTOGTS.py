# IN ORDER AND RECURSIVE SEARCH


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  


def searchT(root, l, d):
    if root:
        if root.left:
            searchT(root.left, l,d)
        l.append(root.val)
        d[root.val]=len(l)-1
        if root.right:
            searchT(root.right, l,d)
    return l,d

def search1(root):
    d={}
    return searchT(root, [], d)


class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        a, d=search1(root)
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.val=sum(a[d[node.val] :])
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return root
                
        

        