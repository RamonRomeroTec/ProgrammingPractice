class Solution(object):
    def getAllElements(self, root1, root2):
        s1=[root1]
        a=[]
        while s1:
            n = s1.pop()
            if n:
                a.append(n.val)
                if n.left:
                    s1.append(n.left)
                if n.right:
                    s1.append(n.right)
        s1=[root2]
        while s1:
            n = s1.pop()
            if n:
                a.append(n.val)
                if n.left:
                    s1.append(n.left)
                if n.right:
                    s1.append(n.right)
        return sorted(a)
        