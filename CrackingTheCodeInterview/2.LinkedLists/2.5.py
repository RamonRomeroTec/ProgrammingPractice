#NO USAR CICLOS; la recursion es la forma mas facil de abreaer un problemas,
#hacer corrida inicial en board

#Identificar atributos base de Clase:: LINKED LIST

#si usamos un nodo actual, se ejecuta la operacion primero

#La alternativa con mayor mantenabilidad es un gothru -> list -> int >> Sumar

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

def tolist(node):
    a=[]
    return auxToList(node, a)

def auxToList(node, a):
    a.append(node.value)
    if node.next==None:
        return a
    else:
        return auxToList(node.next, a)




def sumlist(n1,n2,a,extra):#init 00
    if n1==None:
        sum=extra+0
    else:
        sum=extra+n1.value

    if n2==None:
        sum=sum+0
    else:
        sum=sum+n2.value




    if sum>9:
        extra=int(sum/10)
        sum=sum%10
    else:
        extra=0
    #print("s",sum, extra)


    a.append(sum)


    if n1==None and n2==None:

        return a

    else:
        if n1==None:
            return sumlist(None,n2.next,a,extra)

        elif n2==None:
            return sumlist(n1.next,None,a,extra)

        else:
            return sumlist(n1.next,n2.next,a,extra)


def funappend(n1,n2):
    if n1.next==None:
        n1.next=n2
        return n1
    else:
        return funappend(n1.next,n2)

def funappend(n1):
    if n1.next==None:
        n1.next=n2
    else:
        funappend(n1.next,n2)




if __name__ == '__main__':
    '''
    t4=ListNode(4,None)
    t3=ListNode(2,t4)
    t2=ListNode(2,t3)
    t1=ListNode(5, t2)
    h=ListNode(3, t1)
    '''
    n1=ListNode(1, ListNode(2, ListNode(3, ListNode(4,None))))
    n2=ListNode(9, ListNode(5, ListNode(9, None)))

    '''
    a=set()
    deleterepeatedunsorted(h, a)
    gothru(h)
    '''
    print(tolist(n1))
    print("\n--->")
    print(tolist(n2))
    print("\n--->")
    a=tolist(n1)[::-1]
    b=tolist(n2)[::-1]
    a=map(str,a)
    b=map(str,b)
    a="".join(a)
    b="".join(b)

    a=int(a)
    b=int(b)
    print(a+b)





    #print(sumlist(n1,n2,[],0))

    print(sumlist(n1,n2,[],0)[::-1])
