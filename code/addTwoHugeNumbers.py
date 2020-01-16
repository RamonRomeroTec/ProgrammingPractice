# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
'''

You're given 2 huge integers represented by linked lists.
Each linked list element is a number from 0 to 9999 that represents
a number with exactly 4 digits. The represented number might have leading zeros.
Your task is to add up these huge integers and return the result in the same format.

'''

def gmin(u,d):
    if len(u)<=len(d):
        return u
    return d
def addTwoHugeNumbers(a, b):
    ha=a
    s1=[]
    while a!= None:
        s1.append(a.value)
        a=a.next
    hb=b
    s2=[]
    while b!= None:
        s2.append(b.value)
        b=b.next
    update=gmin(s1,s2)

    for i in range(0,abs(len(s1)-len(s2))):
        update.insert(0,0)

    carry=0
    n=[]
    for i in range(1,len(s1)+1):
        a=s1[-i]+s2[-i]+carry
        if int(a/10000)!=0:
            carry=int(a/10000)
            a=a%10000
        else:
            carry=0

        n.append(a)
    if carry!=0:
        n.append(carry)

    n=n[::-1]
    return n
