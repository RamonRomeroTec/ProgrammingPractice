

class Node(object):
    """docstring for [object Object]."""
    def __init__(self, val=None, lnodes=None):
        self.val=val
        self.nodes=lnodes

    def __str__(self):
        return str(self.val)


class Graph(object):
    def __init__(self, arg):
        self.nodes=arg



from collections import deque

def auxb(node, marked):
    queue = deque([])
    marked.append(node)
    queue.append(node)
    while len(queue)>0:
        r=queue.popleft()
        print(r)
        for i in r.nodes:
            if i not in marked:
                marked.append(i)
                queue.append(i)

def breadth(node):
    marked=[]
    auxb(node, marked)


def auxa(node, visited):
    if node == None:
        return 0
    print (node.value)
    visited.append(node)
    for i in node.nodes:
        if i not in visited:
            return auxsearch(i,visited)

def depth(node):
    v=[]
    return auxa(node,v)



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

    breadth(a)
