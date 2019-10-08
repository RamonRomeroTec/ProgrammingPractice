class Solution(object):
    def findMode(self, root):
        d={}
        s = [root]
        while s:
            node=s.pop()
            if node:
                if node.val in d:
                    d[node.val]+=1
                else:
                    d[node.val]=1
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
        modek=[]
        modev=0
        for k, v in d.items():
            if v > modev:
                modev=v
                modek=[k]
            elif v == modev:
                modek.append(k)
        return modek
                    
        