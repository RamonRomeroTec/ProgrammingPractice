class Node:
    def __init__(self, v):
        self.left=None
        self.right=None
        self.val=v

a=Node(3)
a.left = Node(2)
a.left.left = Node(1)

a.right = Node(4)
a.right.right = Node(5)

def traverse(root):
    ans=[]
    aux(root, ans)
    return ans

def aux(root, ans):
    if root:
        aux(root.left, ans)
        ans.append(root.val)
        aux(root.right, ans)

print(traverse(a))