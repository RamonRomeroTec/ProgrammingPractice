# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        stack = [(root, 0)]
        maxi=-1
        while stack:
            x=stack.pop()
            node=x[0]
            d=x[1]
            maxi=max(d,maxi)
            if node:
                if node.right:
                    stack.append((node.right, d+1))
                if node.left:
                    stack.append((node.left, d+1))
        print(maxi)
            
        the_intersection=[]
        stack = [(root,[], 0)]
        while stack:
            x=stack.pop()
            node, path, deep = x[0], x[1], x[2]
            if node:
                if maxi==deep:
                    the_intersection.append((path, node))
                aux=path[:]
                aux.append(node.val)
                if node.left:
                    stack.append((node.left, aux, deep+1))
                if node.right:
                    stack.append((node.right, aux, deep+1))
        if len(the_intersection)==1:
            return the_intersection[0][1]
            
        s=set(the_intersection[0][0])
        for i in range(len(the_intersection)):
            s=s&set(the_intersection[i][0])
            
            
        au=[root]
        while au:
            x=au.pop()
            node=x
            if node:
                print(s, node.val)
                if node.val in s:
                    s.remove(node.val)
                if len(s)==0:
                    return node
                if node.right:
                    au.append(node.right)
                if node.left:
                    au.append(node.left)
        
        return root