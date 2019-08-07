# in trees consider as case base the structure of the tree, not to traverse

class Solution(object):
    def trimBST(self, root, L, R):
        

        return self.trim(root , L, R)
    
    def trim(self, node,  L, R):
        if not node:
            return None
        elif node.val > R:
            return self.trim(node.left, L, R)
        elif node.val < L:
            return self.trim(node.right, L, R)
        else:
            node.left = self.trim(node.left, L, R)
            node.right = self.trim(node.right, L, R)
            return node