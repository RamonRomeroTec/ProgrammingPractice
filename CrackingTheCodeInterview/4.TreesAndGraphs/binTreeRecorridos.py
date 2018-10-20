'''




      5
  2       8
1   3   6   10






'''


class BinTreeNode(object):
    """docstring for [object Object]."""
    def __init__(self, v,l=None, r=None):
        self.value = v
        self.left = l
        self.right = r


def inOrderTransversal(node):
    if node!=None:
        inOrderTransversal(node.left)
        print(node.value)
        inOrderTransversal(node.right)

def preOrderTransversal(node):    #Profundidad
    if node!=None:
        print(node.value)
        preOrderTransversal(node.left)
        preOrderTransversal(node.right)


def postOrderTransversal(node):
    if node!=None:
        preOrderTransversal(node.left)
        preOrderTransversal(node.right)
        print(node.value)


if __name__ == '__main__':
    a=BinTreeNode(1)
    c=BinTreeNode(3)
    b=BinTreeNode(2,a,c)
    f=BinTreeNode(6)
    g=BinTreeNode(10)
    e=BinTreeNode(8,f,g)
    d=BinTreeNode(5,b,e)
    print("InOrder")
    inOrderTransversal(d)
    print("PreOrder")
    preOrderTransversal(d)
    print("PostOrderTransversal")
    postOrderTransversal(d)
