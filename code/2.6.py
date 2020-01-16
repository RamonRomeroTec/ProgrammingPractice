'''
Palindrome: Implement a function to check if a linked list is a palindrome.
'''

#again if it we are lookin for readability and maintainance
#convert to string and compare is easier than go in a stack or copare by half at the end we ll go in list

class ListNode(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

    def __str__(self):
        return str(self.value)


def tolist(node):
    a=[]
    return auxToList(node, a)


def auxToList(node, a):
    a.append(node.value)
    if node.next==None:
        return a
    else:
        return auxToList(node.next, a)





if __name__ == '__main__':
    '''
    t4=ListNode(4,None)
    t3=ListNode(2,t4)
    t2=ListNode(2,t3)
    t1=ListNode(5, t2)
    h=ListNode(3, t1)
    '''
    n1=ListNode('a', ListNode('b', ListNode('c', ListNode('c', ListNode('b', ListNode('b', ListNode('a', None)))))))

    '''
    a=set()
    deleterepeatedunsorted(h, a)
    gothru(h)
    '''
    print(tolist(n1)==tolist(n1)[::-1])
    print("\n--->")
