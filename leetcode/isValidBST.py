class Solution(object):
    def isValidBST(self, root):
        # def get_arr(node):
        #     a=[]
        #     if node:
        #         a= get_arr(node.left)
        #         a.append(node.val)
        #         a+=(get_arr(node.right))
        #     return a
        # a=get_arr(root)
        # for i in range(len(a)-1):
        #     if a[i]>=a[i+1]:
        #         return False
        # return True
        if not root:
            return True
        stack = [(root,float('-inf'),float('inf'))]
        while stack:
            node,left,right = stack.pop()
            if left>=node.val or right<=node.val:
                return False
            if node.left:
                stack.append((node.left,left,node.val))
            if node.right:
                stack.append((node.right,node.val,right))
        return True
            
        