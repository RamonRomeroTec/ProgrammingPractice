#when we are talking about sets operations always use a set
class ListNode(object):
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

    def __str__(self):
        return str(self.value)


def toset(n):
    a=set()
    return auxtoset(n,a)

def auxtoset(n, a):
    a.add(n)
    if n.next==None:
        return a
    else:
        return auxtoset(n.next,a)

def getintersect(n1, n2):
    s=toset(n1)
    while 1:
        if n2.next==None:
            return "NO"
        else:
            if n2 in s:
                return n2
            else:
                n2=n2.next



if __name__ == '__main__':
    t4=ListNode(4,None)
    t3=ListNode(2,t4)
    t2=ListNode(999,t3)
    t1=ListNode(5, t2)
    h=ListNode(3, t1)
    x2=ListNode(7,t2)
    x1=ListNode(5,x2)
    h2=ListNode(4,x1)


    print(getintersect(h, h2))
