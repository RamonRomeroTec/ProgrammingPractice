
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        h1, h2 =l1, l2
        last1=None
        last2 = None
        len1=0
        len2=0
        while l1:
            len1+=1
            if l1.next==None:
                last1=l1
            l1=l1.next  
        while l2:
            len2+=1
            if l2.next==None:
                last2=l2
            l2=l2.next
        l1 = h1
        l2 = h2
        carry=0
        if len1>=len2:
            while l1:
                s1=l1.val
                try:
                    s2 = l2.val
                except:
                    s2 = 0
                sum_value = s1+s2+carry
                if sum_value>9:
                    carry=sum_value//10
                    sum_value=sum_value%10
                else:
                    carry=0
                print(sum_value)
                l1.val=sum_value
                l1=l1.next
                if l2:
                    l2=l2.next
            if carry:
                last1.next=ListNode(carry)
            return h1
        
        else:
            while l2:
                s2=l2.val
                try:
                    s1 = l1.val
                except:
                    s1 = 0
                sum_value = s1+s2+carry
                if sum_value>9:
                    carry=sum_value//10
                    sum_value=sum_value%10
                else:
                    carry=0
                l2.val=sum_value
                l2=l2.next
                if l1:
                    l1=l1.next
            if carry:
                last2.next=ListNode(carry)
            return h2
            