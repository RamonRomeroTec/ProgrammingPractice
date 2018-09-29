# LAS FUNCIONES RECURSIVAS EN PYTHON SIEMPRE DEBEN DE TENER UN return
'''

Remove Dups: Write code to remove duplicates from an unsorted li nked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed? Hints: #9, #40
'''
class ListNode(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

    def __str__(self):
        return str(self.value)

    def gnext(self):
        return self.next


def gothru(node):

    print(node.value)
    if node.next==None:
        print("finished")


    else:
        gothru(node.next)
'''
def gothrudel(node, r):

    if node.next==None:
        print("finished")


    if (node.next.val) not in s:
        s.add()
        gothrudel(node.next)
    else:
        node.next=node.next.next
        gothrudel(node)


'''

def find_next(node, v):
    if node.next.value!=v:
        return node.next
    else:
        if node.next==None:

            return None
        else:
            return find_next(node.next, v)


def deleterepeatedunsorted(node, traveled):
    if node.next==None:
        print("Deleted repeated")
    else:
        traveled.add(node.value)
        if node.next.value in traveled: # el siguiente esta repetido
            node.next=find_next(node, node.next.value)
            if node.next==None:
                print("Deleted repeateds")
            else:
                deleterepeatedunsorted(node.next, traveled)

        else:
            deleterepeatedunsorted(node.next, traveled)

            #deleteit

def deleterepeatedunsortedNoBuff(node):
    cur=node.value
    if node.next==None:
        print("Deleted repeated")
    else:
        if node.next.value in traveled: # el siguiente esta repetido
            node.next=find_next(node, node.next.value)
            if node.next==None:
                print("Deleted repeateds")
        else:
            deleterepeatedunsorted(node.next, traveled)



if __name__ == '__main__':
    '''
    t4=ListNode(4,None)
    t3=ListNode(2,t4)
    t2=ListNode(2,t3)
    t1=ListNode(5, t2)
    h=ListNode(3, t1)
    '''
    h2=ListNode(0,ListNode(2,ListNode(2,ListNode(2, ListNode(5, ListNode(2, ListNode(3, None)))))))
    '''
    a=set()
    deleterepeatedunsorted(h, a)
    gothru(h)
    '''
    b=set()
    deleterepeatedunsorted(h2, b)

    gothru(h2)
