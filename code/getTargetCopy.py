class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        s1=[(original, [])]
        while s1:
            e1, p1 =s1.pop()
            if e1 is target:
                for i in range(len(p1)):
                    if p1[i]==1:
                        cloned=cloned.right
                    else:
                        cloned=cloned.left
                return cloned  
            else:
                if e1.left:
                    aux=p1[:]
                    aux.append(0)
                    s1.append((e1.left, aux ))
                if e1.right:
                    aux=p1[:]
                    aux.append(1)
                    s1.append((e1.right, aux ))