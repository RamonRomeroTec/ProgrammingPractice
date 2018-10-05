class Node(object):
    def __init__(self, id=None, nodes=None):
        self.id = id
        self.nodes=nodes


if __name__ == '__main__':
    a=Node('a')
    b=Node('b')
    c=Node('c')
    d=Node('d')
    e=Node('e')
    f=Node('f')
    g=Node('g')
    h=Node('h')
    i=Node('i')
    j=Node('j')
    a.nodes=[b,c]
    b.nodes=[e,d]
    d.nodes=[f]
    c.nodes=[g,h,i]
    g.nodes=[j]
    h.nodes=[j]
    i.nodes=[j]
