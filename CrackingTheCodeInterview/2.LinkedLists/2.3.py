
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




def byIndex(node, target):
    aux1(node, target, 1)

def aux1(node, target, counter):
    if node.next==None:
        print("ok")
    else:
        if counter+1==target:
            node.next=node.next.next
            print("ok")

        else:
            aux1(node.next, target, counter+1)



def byContent(node, target):
    if node.next==None:
        print("ok")
    else:
        if node.next.value==target:
            node.next=node.next.next
            print("ok")

        else:
            byContent(node.next, target)


if __name__ == '__main__':
    '''
    t4=ListNode(4,None)
    t3=ListNode(2,t4)
    t2=ListNode(2,t3)
    t1=ListNode(5, t2)
    h=ListNode(3, t1)
    '''
    h2=ListNode(0,ListNode(1,ListNode(2,ListNode(3, ListNode(4, ListNode(5, ListNode(5, None)))))))
    '''
    a=set()
    deleterepeatedunsorted(h, a)
    gothru(h)
    '''
    gothru(h2)
    byIndex(h2, 2)
    print("\n--->")
    gothru(h2)



    h3=ListNode('a',ListNode('b',ListNode('c',ListNode('d', ListNode('e', ListNode('f', ListNode('g', None)))))))
    '''
    a=set()
    deleterepeatedunsorted(h, a)
    gothru(h)
    '''
    gothru(h3)
    byContent(h3, 'c')
    print("\n--->")
    gothru(h3)
