


class Node(object):
    """docstring for [object Object]."""
    def __init__(self, val=None, lnodes=None):
        self.val=val
        self.nodes=lnodes


class Graph(object):
    def __init__(self, arg):
        self.nodes=arg


if __name__ == '__main__':

    a=Node(0)
    b=Node(1)
    c=Node(2)
    d=Node(3)
    e=Node(4)
    f=Node(5)
    g=Node(6)
    a.nodes=[b]
    b.nodes=[c]
    c.nodes=[a,d]
    d.nodes=[c]
    e.nodes=[g]
    f.nodes=[e]
    g.node=[f]

    ns=[a,b,c,d,e,f,g]

    g=Graph(ns)
