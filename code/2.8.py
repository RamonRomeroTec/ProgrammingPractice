'''

Loop Detection: Given a circular linked list, implement an algorithm that
returns the node at the beginning of the loop.

DEFINI TION

Circular linked list: A (corrupt) linked list in which a node's next pointer
points to an earlier node, so as to make a loop in the linked list.

'''

class ListNode(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

    def __str__(self):
        return str(self.value)



def gothru(node):

    print(node.value)
    if node.next==None:
        print("finished")


    else:
        gothru(node.next)


def getLast(n):
    a=set()
    return auxgetLast(n,a)

def auxgetLast(n, a):
    if n.next==None:
        return -1
    else:
        if n in a:
            return n
        else:
            a.add(n)
            return auxgetLast(n.next,a)

if __name__ == '__main__':
    h=ListNode(777)
    uh2=ListNode(33, h)
    uh=ListNode(4, uh2)
    t4=ListNode(4,h)
    t3=ListNode(2,t4)
    t2=ListNode(999,t3)
    t1=ListNode(5, t2)
    h.next=t1


    print(getLast(uh))
