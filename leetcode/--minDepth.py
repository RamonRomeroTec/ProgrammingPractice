# get vision from far away, check and review per level, aka leveled search
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        depth = 1
        queue = collections.deque([root])
        while queue:
            aux=len(queue)
            for i in range(aux):
                node = queue.popleft()
                if (not node.left) and (not node.right):
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1