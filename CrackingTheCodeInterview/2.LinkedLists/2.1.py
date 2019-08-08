# LAS FUNCIONES RECURSIVAS EN PYTHON SIEMPRE DEBEN DE TENER UN return
'''

Remove Dups: Write code to remove duplicates from an unsorted li nked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed? Hints: #9, #40
'''
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def gnext(self):
        return self.next


def gothru(node):

    print(node.val)
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
    if node.next.val!=v:
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
        traveled.add(node.val)
        if node.next.val in traveled: # el siguiente esta repetido
            node.next=find_next(node, node.next.val)
            if node.next==None:
                print("Deleted repeateds")
            else:
                deleterepeatedunsorted(node.next, traveled)

        else:
            deleterepeatedunsorted(node.next, traveled)

            #deleteit

def deleterepeatedunsortedNoBuff(node):
    cur=node.val
    if node.next==None:
        print("Deleted repeated")
    else:
        if node.next.val in traveled: # el siguiente esta repetido
            node.next=find_next(node, node.next.val)
            if node.next==None:
                print("Deleted repeateds")
        else:
            deleterepeatedunsorted(node.next, traveled)








def aux(A,s,l):

    print(A.val not in s, A.val, s, l)
    if A.val not in s:
        s.add(A.val)
        l.append(A)


    if A.next==None:
        return l
    else:
        return aux(A.next,s,l)

def gen(l):
    if len(l)>1:

        for i in range(len(l)-1):
            l[i].next=l[i+1]


        l[-1].next=None
        a=

        print(l[-1].val, l[-1].next, "af")


        print(l[0].val, l[0].next, "l")
        print(l[1].val, l[1].next, "lm")
        print(l[-1].val, l[-1].next, "lm")

        return l[0]

    else:
        l[0].next=None
        return l[0]



class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        while A:
            while A.next and A.next.val == A.val:
                A.next = A.next.next
            A = A.next
        return head
    '''
    def deleteDuplicates(self, A):
        s=set()
        l=[]
        a=aux(A, s, l)
        print(a)

        return gen(a)
    '''

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


    h5=ListNode(19,ListNode(19,ListNode(20,ListNode(20, ListNode(20, ListNode(20, ListNode(20, None)))))))
    print(gothru(Solution().deleteDuplicates(h5)))
