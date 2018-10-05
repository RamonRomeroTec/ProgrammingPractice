

class BinTreeNode(object):
    """docstring for [object Object]."""
    def __init__(self, v,l=None, r=None):
        self.value = v
        self.left = l
        self.right = r


def findhalf(l):
    a=len(l)
    index=int(a/2)
    if a>0:
        n=BinTreeNode(l[index])
        n.left=findhalf(l[:index])
        n.right=findhalf(l[index+1:])
        return n
    else:
        return None



if __name__ == '__main__':

    a=[1,2,3,5,6,8,10]
    print (findhalf(a).value)
    print (findhalf(a).left)
    print (findhalf(a).right)

'''




      5
  2       8
1   3   6   10





'''
