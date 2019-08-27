class Solution(object):
    def maxLevelSum(self, root):
        maxi=0
        sl=0
        q = collections.deque([root])
        l=0
        while q:
            current = len(q)
            l+=1
            suma=0
            for i in range(0, current):
                node = q.popleft()
                suma=suma+node.val
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if suma>maxi:
                maxi=suma
                sl=l
        return sl
