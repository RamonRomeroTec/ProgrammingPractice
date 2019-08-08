
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





def getk(node, target):
    return auxgetk(node, target, 1)

def auxgetk(node, target, counter):
    if node.next==None:
        return None
    else:
        if target==counter:
            return node
        else:

            return auxgetk(node.next, target, counter+1)

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
    print(getk(h2, 2))
    print(getk(h2, 5))
