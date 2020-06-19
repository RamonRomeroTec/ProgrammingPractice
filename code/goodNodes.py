class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxi = root.val
        s=[(root, maxi)]
        c=1
        while s:
            node, current = s.pop()
            if node:
                if node.left:
                    a= node.left.val
                    if a >= current:
                        c+=1
                    else:
                        a=current
                    s.append((node.left, a))
            
                if node.right:
                    a= node.right.val
                    if a >= current:
                        c+=1
                    else:
                        a=current
                    s.append((node.right, a))
        return c
                    